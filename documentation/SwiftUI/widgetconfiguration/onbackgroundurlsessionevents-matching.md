# onBackgroundURLSessionEvents(matching:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func onBackgroundURLSessionEvents(matching matchingBlock: ((String) -> Bool)? = nil, _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void) -> some WidgetConfiguration
```

#### Return Value

A widget that triggers `urlSessionEvent` when events are generated for a `URLSession` with the specified identifier.

#### Discussion

When a widget initiates a background network request, the system delivers events related to the request directly to the widget extension instead of the containing app. To process the events, do the following:

1. Use the `identifier` parameter to determine if a corresponding `URLSession` object exists. If the system hasn’t terminated your widget extension, maintain a reference to the same `URLSession` object you used for the original background network request. If the system terminated your widget extension, use the identifier to create a new `URLSession` object so it can receive the events. You might consider lazily initializing, and caching, the `URLSession` objects in a central location so that your code works regardless of whether your extension remains active, is suspended, or is terminated.
2. Store a reference to the `completion` closure to invoke it after the system delivers all events.
3. After the system calls the `URLSession` delegate’s [`urlSessionDidFinishEvents(forBackgroundURLSession:)`](https://developer.apple.com/documentation/Foundation/URLSessionDelegate/urlSessionDidFinishEvents(forBackgroundURLSession:)) method, invoke the `completion` closure.

## Parameters

- `urlSessionEvent`: A closure that takes a string parameter called    and a closure called  .

## See Also

- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some WidgetConfiguration](widgetconfiguration/backgroundtask(_:action:).md)
  Runs the given action when the system provides a background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/onbackgroundurlsessionevents(matching:_:))*