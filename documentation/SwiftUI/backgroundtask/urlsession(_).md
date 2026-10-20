# urlSession(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A task that responds to background URL sessions matching the given identifier.

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
static func urlSession(_ identifier: String) -> BackgroundTask<Void, Void>
```

#### Return Value

A background task that you can handle with your app or extension.

## Parameters

- `identifier`: The identifier to match.

## See Also

### Responding to URL sessions
- [static var urlSession: BackgroundTask<String, Void>](./urlsession.md)
  A task that responds to background URL sessions.
- [static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String, Void>](./urlsession%28matching%29.md)
  A task that responds to background URL sessions matching the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession(_:))*