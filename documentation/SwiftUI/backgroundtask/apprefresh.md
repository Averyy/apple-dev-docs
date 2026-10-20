# appRefresh

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A task that updates your app’s state in the background.

**Availability**:
- watchOS 9.0+

> **Deprecated**: Use appRefresh(_ identifier: String)

## Declaration

```swift
static var appRefresh: BackgroundTask<String?, Void> { get }
```

## See Also

### Refreshing the app
- [static func appRefresh(String) -> BackgroundTask<Void, Void>](./apprefresh%28_%29.md)
  A task that updates your app’s state in the background for a matching identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/apprefresh)*