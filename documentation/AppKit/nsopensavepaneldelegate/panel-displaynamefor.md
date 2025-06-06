# panel(_:displayNameFor:)

**Framework**: AppKit  
**Kind**: method

`NSSavePanel`: Optional — Sent when the content type popup is displayed and the save panel needs the display name for a type. If `nil` is returned, the save panel will display type’s `localizedDescription`. `NSOpenPanel`: Not sent.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, displayNameFor type: UTType) -> String?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:displaynamefor:))*