# urlSession(matching:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func urlSession(matching: @escaping @Sendable (String) -> Bool) -> BackgroundTask<String, Void>
```

## Return Value

A background task that you can handle with your app or extension.

## Parameters

- `matching`: The predicate to match.

## See Also

### Responding to URL sessions
- [static var urlSession: BackgroundTask<String, Void>](./urlsession.md)
  A task that responds to background URL sessions.
- [static func urlSession(String) -> BackgroundTask<Void, Void>](./urlsession%28_%29.md)
  A task that responds to background URL sessions matching the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession(matching:))*