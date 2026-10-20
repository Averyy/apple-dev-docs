# panel(_:didSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

`NSSavePanel`: Optional — Sent when the user changes the current type. `NSOpenPanel`: Not sent.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, didSelect type: UTType?)
```

```objc
- (void) panel:(id) sender didSelectType:(UTType *) type;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:didselect:))*