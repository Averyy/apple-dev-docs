# isDiscoverable

**Framework**: App Intents  
**Kind**: property

A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static var isDiscoverable: Bool { get }
```

#### Discussion

App Intents must be discoverable to support App Shortcuts. If your app intent isn’t discoverable, people can use it only when it’s directly connected by a button in a SwiftUI app or a widget.

This property is `true` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptysnippetintent/isdiscoverable-44ooy)*