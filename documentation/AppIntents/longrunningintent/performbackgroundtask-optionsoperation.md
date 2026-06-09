# performBackgroundTask(options:operation:)

**Framework**: App Intents  
**Kind**: method

Runs an operation in the background with an extended amount of time.

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
@discardableResult
func performBackgroundTask<T>(options: LongRunningTaskOptions = [], operation: @escaping () async throws -> T) async throws -> T
```

#### Return Value

The value you return from the `operation` closure.

#### Discussion

> **Note**: Throws an error if the operation fails or the system can’t run the operation.

Use this method to wrap long-running code in your app intent’s [`perform()`](appintent/perform().md) method. This method automatically extends the amount of time your code has to run in the background past the standard 30-second limit present on some platforms. You don’t have to start a separate background task.

While your operation runs, provide regular progress updates using the [`progress`](progressreportingintent/progress.md) property of the [`ProgressReportingIntent`](progressreportingintent.md) protocol. If you don’t update this property regularly, the system can cancel the background runtime extension and end your task prematurely.

Live Activities displays the progress of your app intent’s task using information it receives automatically from this method. Live Activities displays the values of the [`localizedDescription`](https://developer.apple.com/documentation/Foundation/Progress/localizedDescription) and [`localizedAdditionalDescription`](https://developer.apple.com/documentation/Foundation/Progress/localizedAdditionalDescription) properties as the title and subtitle of your task. It also displays a progress bar, which it configures using the values in the [`completedUnitCount`](https://developer.apple.com/documentation/Foundation/Progress/completedUnitCount) and [`totalUnitCount`](https://developer.apple.com/documentation/Foundation/Progress/totalUnitCount) properties.

The following example shows the [`perform()`](appintent/perform().md) method of an app intent, which uses this method to extend the background runtime of the task. The method implementation uploads a file in chunks and updates progress values after each chunk.

```swift
func perform() async throws -> some IntentResult & ReturnsValue<String> {
    let result = try await performBackgroundTask {
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
```

## Parameters

- `options`: Additional options to configure the runtime behavior. For example, you might use this parameter to tell the system that your task requires GPU resources. The default value for this parameter is an empty set.
- `operation`: The closure to run in the background. Use this closure to specify the code for your app intent’s task. The closure takes no parameters and returns a type that you specify.

## See Also

- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T, onCancel: (IntentCancellationReason) -> Void) async throws -> T](longrunningintent/performbackgroundtask(options:operation:oncancel:).md)
  Runs an operation in the background and provides a way to cancel the operation before it finishes.
- [struct LongRunningTaskOptions](longrunningtaskoptions.md)
  Options for configuring long-running tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/longrunningintent/performbackgroundtask(options:operation:))*