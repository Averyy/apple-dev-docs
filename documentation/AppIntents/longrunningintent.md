# LongRunningIntent

**Framework**: App Intents  
**Kind**: protocol

An interface you use to extend the background execution time of an app intent that performs a long-running task.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol LongRunningIntent : ProgressReportingIntent
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

This protocol allows an app intent to run for an extended period of time in the background. When a task runs in the background, the system traditionally gives it up to 30 seconds to finish its task. For some types of tasks, this amount of time can be insufficient to complete the task. For example, file operations, data synchronization, machine learning inference, and data processing tasks can take longer if they operate on a sufficiently large amount of data. If your app intent performs a task that might exceed the built-in time limits, incorporate this protocol and use its methods to perform that task.

In the implementation of your app intent, place the code for your task inside one of the methods this protocol offers. The methods of this protocol work with the system to extend the amount of time your code has to run. While your code runs, the system requires you to report progress regularly, which you do using the [`progress`](progressreportingintent/progress.md) property of the inherited [`ProgressReportingIntent`](progressreportingintent.md) protocol. If you don’t update this property regularly, the system can cancel the background runtime extension and end your task prematurely.

The following example shows the implementation of an app intent that uploads a file. The implementation uploads the file in chunks, and updates the [`progress`](progressreportingintent/progress.md) property after each chunk.

```swift
struct UploadFileIntent: LongRunningIntent {
    static var title: LocalizedStringResource = "Upload Large File"

    @Parameter(title: "File")
    var file: IntentFile

    func perform() async throws -> some IntentResult & ReturnsValue<String> {
        // Use performBackgroundTask - zero required parameters!
        let result = try await performBackgroundTask {
            // This code runs with extended execution time
            progress.totalUnitCount = 100
            progress.localizedDescription = "Uploading file"

            for chunk in 0..<100 {
                try Task.checkCancellation()
                await uploadChunk(chunk)
                progress.completedUnitCount = Int64(chunk + 1)
                progress.localizedAdditionalDescription = "\(chunk + 1)% complete"
            }
            return "Upload complete!"
        }

        return .result(value: result)
    }

    private func uploadChunk(_ chunk: Int) async {
        // Simulate uploading a chunk
    }
}
```

> **Note**: In macOS, the system allows background tasks to run without time limits. In iOS, iPadOS, tvOS, visionOS, and watchOS, the system gives tasks 30 seconds to run in the background unless you use the methods of this protocol to extend that runtime.

## Topics

### Performing background tasks
- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T) async throws -> T](longrunningintent/performbackgroundtask(options:operation:).md)
  Runs an operation in the background with an extended amount of time.
- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T, onCancel: (IntentCancellationReason) -> Void) async throws -> T](longrunningintent/performbackgroundtask(options:operation:oncancel:).md)
  Runs an operation in the background and provides a way to cancel the operation before it finishes.
- [struct LongRunningTaskOptions](longrunningtaskoptions.md)
  Options for configuring long-running tasks.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [ProgressReportingIntent](progressreportingintent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol UndoableIntent](undoableintent.md)
  An interface you use to register undoable actions in your app intent code.
- [protocol CancellableIntent](cancellableintent.md)
  An interface to support the graceful cancellation of your app intent’s task.
- [protocol PredictableIntent](predictableintent.md)
  An interface that indicates the system can suggest the intent as a potential action to run.
- [struct IntentPrediction](intentprediction.md)
  A prediction for an app intent that the system might display to someone when it’s relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/longrunningintent)*