# appRefresh(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A task that updates your app’s state in the background for a matching identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func appRefresh(_ identifier: String) -> BackgroundTask<Void, Void>
```

## Return Value

A background task that you can handle with your app or extension.

## Parameters

- `identifier`: The identifier to match.

## See Also

### Refreshing the app
- [static var appRefresh: BackgroundTask<String?, Void>](./apprefresh.md)
  A task that updates your app’s state in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask/apprefresh(_:))*