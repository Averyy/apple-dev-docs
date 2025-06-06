# backgroundTask(_:action:)

**Framework**: SwiftUI  
**Kind**: method

Runs the specified action when the system provides a background task.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func backgroundTask<D, R>(_ task: BackgroundTask<D, R>, action: @escaping (D) async -> R) -> some Scene where D : Sendable, R : Sendable
```

#### Discussion

When the system wakes your app or extension for one or more background tasks, it will call any actions associated with matching tasks. When your async actions return, the system put your app back into a suspended state. The system considers the task completed when the action closure that you provide returns. If the action closure has not returned when the task runs out of time to complete, the system cancels the task. Use doc://com.apple.documentation/documentation/Swift/withTaskCancellationHandler(operation:onCancel:) to observe whether the task is low on runtime.

```swift
/// An example of a Weather Application.
struct WeatherApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Responds to App Refresh")
        }
        .backgroundTask(.appRefresh("WEATHER_DATA")) {
            await updateWeatherData()
        }
    }
    func updateWeatherData() async {
        // fetches new weather data and updates app state
    }
}
```

## Parameters

- `task`: The type of task with which to associate the provided action.
- `action`: An async closure that the system runs for the specified task   type.

## See Also

- [struct BackgroundTask](backgroundtask.md)
  The kinds of background tasks that your app or extension can handle.
- [struct SnapshotData](snapshotdata.md)
  The associated data of a snapshot background task.
- [struct SnapshotResponse](snapshotresponse.md)
  Your appplication’s response to a snapshot background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/backgroundtask(_:action:))*