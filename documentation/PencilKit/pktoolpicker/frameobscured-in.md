# frameObscured(in:)

**Framework**: PencilKit  
**Kind**: method

Returns the portion of the specified view that the tool picker obscures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func frameObscured(in view: UIView) -> CGRect
```

#### Return Value

The portion of `view` (in its own coordinate space) obscured by the palette.

#### Discussion

Because the palette is transparent in places, part of your view’s content may continue to show through in the specified rectangle.

## Parameters

- `view`: The view that’s potentially obscured by the tool picker’s palette.

## See Also

- [func setVisible(Bool, forFirstResponder: UIResponder)](pktoolpicker/setvisible(_:forfirstresponder:).md)
  Sets the visibility for the tool picker, based on when the specified responder object becomes active.
- [var isVisible: Bool](pktoolpicker/isvisible.md)
  A Boolean value that indicates whether the tool picker is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/frameobscured(in:))*