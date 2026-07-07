# performBackgroundTask(options:operation:onCancel:)

**Framework**: App Intents  
**Kind**: method

Runs an operation in the background and provides a way to cancel the operation before it finishes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func performBackgroundTask<T>(options: LongRunningTaskOptions = [], operation: @escaping () async throws -> T, onCancel: @escaping @Sendable (IntentCancellationReason) -> Void) async throws -> T where Self : CancellableIntent
```

#### Return Value

The value you return from the `operation` closure.

#### Discussion

> **Note**: Throws an error if the operation fails or the system can’t run the operation.

If your app intent also conforms to the [`CancellableIntent`](cancellableintent.md) protocol, use this method to wrap long-running code in your app intent’s [`perform()`](appintent/perform().md) method. This method automatically extends the amount of time your code has to run in the background past the standard 30-second limit present on some platforms. You don’t have to start a separate background task. If someone cancels the task for any reason, the system runs your cancellation handler before stopping the task.

While your operation runs, provide regular progress updates using the [`progress`](progressreportingintent/progress.md) property of the inherited [`ProgressReportingIntent`](progressreportingintent.md) protocol. If you don’t update this property regularly, the system can cancel the background runtime extension and end your task prematurely.

Live Activities displays the progress of your app intent’s task using information it receives automatically from this method. Live Activities displays the values of the [`localizedDescription`](https://developer.apple.com/documentation/Foundation/Progress/localizedDescription) and [`localizedAdditionalDescription`](https://developer.apple.com/documentation/Foundation/Progress/localizedAdditionalDescription) properties as the title and subtitle of your task. It also displays a progress bar, which it configures using the values in the [`completedUnitCount`](https://developer.apple.com/documentation/Foundation/Progress/completedUnitCount) and [`totalUnitCount`](https://developer.apple.com/documentation/Foundation/Progress/totalUnitCount) properties.

The following example shows the [`perform()`](appintent/perform().md) method of an app intent, which uses this method to extend the background runtime of the task. The method implementation uploads a file in chunks and updates progress values after each chunk. If someone cancels the task, the call to [`checkCancellation()`](https://developer.apple.com/documentation/Swift/Task/checkCancellation()) throws an error that this method catches and uses to run your cancellation handler.

```swift
struct UploadFileIntent: LongRunningIntent, CancellableIntent {
    func perform() async throws -> some IntentResult {
        return try await performBackgroundTask {
            progress.totalUnitCount = 100
            for chunk in 0..<100 {
                try Task.checkCancellation()
                await uploadChunk(chunk)
                progress.completedUnitCount = Int64(chunk + 1)
            }
            return .result()
        } onCancel: { reason in
            cleanup(for: reason)
        }
    }
}
```

## Parameters

- `options`: Additional options to configure the runtime behavior. For example, you might use this parameter to tell the system that your task requires GPU resources. The default value for this parameter is an empty set.
- `operation`: The closure to run in the background. Use this closure to specify the code for your app intent’s task. The closure takes no parameters and returns a type that you specify.
- `onCancel`: The closure to run when cancellation occurs. Use this closure to respond to the cancellation and perform any required cleanup. The closure receives a parameter with the cancellation reason and returns no value. The system runs this closure instead of the [`withIntentCancellationHandler(operation:onCancel:isolation:)`](cancellableintent/withintentcancellationhandler(operation:oncancel:isolation:).md) method from the [`CancellableIntent`](cancellableintent.md) protocol.

## See Also

- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T) async throws -> T](longrunningintent/performbackgroundtask(options:operation:).md)
  Runs an operation in the background with an extended amount of time.
- [struct LongRunningTaskOptions](longrunningtaskoptions.md)
  Options for configuring long-running tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/longrunningintent/performbackgroundtask(options:operation:oncancel:))*