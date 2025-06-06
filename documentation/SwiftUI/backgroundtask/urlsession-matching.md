# urlSession(matching:)

**Framework**: SwiftUI  
**Kind**: method

A task that responds to background URL sessions matching the given predicate.

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
static func urlSession(matching: @escaping (String) -> Bool) -> BackgroundTask<String, Void>
```

#### Return Value

A background task that you can handle with your app or extension.

## Parameters

- `matching`: The predicate to match.

## See Also

- [static var urlSession: BackgroundTask<String, Void>](backgroundtask/urlsession.md)
  A task that responds to background URL sessions.
- [static func urlSession(String) -> BackgroundTask<Void, Void>](backgroundtask/urlsession(_:).md)
  A task that responds to background URL sessions matching the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession(matching:))*