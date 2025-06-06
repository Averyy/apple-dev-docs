# highlight(_:)

**Framework**: AppKit  
**Kind**: method

An action for toggling `NSTextHighlightStyleAttributeName` in the receiver’s selected range. The sender should be a menu item with a `representedObject` of type (`NSTextHighlightColorScheme`).

**Availability**:
- macOS 15.0+

## Declaration

```swift
@IBAction
@MainActor func highlight(_ sender: Any?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/highlight(_:))*