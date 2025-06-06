# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new menu for a collection of app-specific commands, inserted in the standard location for app menus (after the View menu, in order with other menus declared without an explicit location).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(_ name: Text, @ViewBuilder content: () -> Content)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandmenu/init(_:content:))*