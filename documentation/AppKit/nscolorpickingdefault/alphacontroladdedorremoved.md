# alphaControlAddedOrRemoved(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Sent when the color panel’s opacity controls have been hidden or displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func alphaControlAddedOrRemoved(_ sender: Any?)
```

#### Discussion

This method is invoked automatically when the opacity slider of the `NSColorPanel` is added or removed; you never invoke this method directly.

If the color picker has its own opacity controls, it should hide or display them, depending on whether the sender’s [`showsAlpha`](nscolorpanel/showsalpha.md) method returns [`false`](https://developer.apple.com/documentation/swift/false) or [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `sender`: The color panel sending the message.

## See Also

- [func viewSizeChanged(Any?)](nscolorpickingdefault/viewsizechanged(_:).md)
  Tells the recever when the color panel’s view size changes in a way that might affect the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/alphacontroladdedorremoved(_:))*