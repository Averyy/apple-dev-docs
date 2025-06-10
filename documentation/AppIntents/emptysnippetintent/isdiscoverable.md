# isDiscoverable

**Framework**: App Intents  
**Kind**: property

A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var isDiscoverable: Bool
```

#### Discussion

App Intents must be discoverable to support App Shortcuts. If your app intent isn’t discoverable, people can use it only when it’s directly connected by a button in a SwiftUI app or a widget.

This property is `true` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptysnippetintent/isdiscoverable)*