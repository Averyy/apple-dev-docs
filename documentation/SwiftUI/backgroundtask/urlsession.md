# urlSession

**Framework**: SwiftUI  
**Kind**: property

A task that responds to background URL sessions.

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
static var urlSession: BackgroundTask<String, Void> { get }
```

## See Also

- [static func urlSession(String) -> BackgroundTask<Void, Void>](backgroundtask/urlsession(_:).md)
  A task that responds to background URL sessions matching the given identifier.
- [static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String, Void>](backgroundtask/urlsession(matching:).md)
  A task that responds to background URL sessions matching the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession)*