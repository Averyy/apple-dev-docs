# frameObscured(in:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGRect) frameObscuredInView:(UIView *) view;
```

## Return Value

The portion of `view` (in its own coordinate space) obscured by the palette.

## Discussion

Because the palette is transparent in places, part of your view’s content may continue to show through in the specified rectangle.

## Parameters

- `view`: The view that’s potentially obscured by the tool picker’s palette.

## See Also

### Coordinating the visibility of the picker
- [func setVisible(Bool, forFirstResponder: UIResponder)](./setvisible%28_,forfirstresponder%29.md)
  Sets the visibility for the tool picker, based on when the specified responder object becomes active.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the tool picker is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/frameobscured(in:))*