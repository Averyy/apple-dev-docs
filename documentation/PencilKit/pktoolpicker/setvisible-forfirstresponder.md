# setVisible(_:forFirstResponder:)

**Framework**: PencilKit  
**Kind**: method

Sets the visibility for the tool picker, based on when the specified responder object becomes active.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setVisible(_ visible: Bool, forFirstResponder responder: UIResponder)
```

#### Discussion

Each time you call this method with the `visible` parameter set to [`true`](https://developer.apple.com/documentation/Swift/true), the tool picker adds `responder` to a list of objects to monitor. When any object in the list becomes the first responder, the tool picker displays the palette. Calling this method with the `visible` parameter set to [`false`](https://developer.apple.com/documentation/Swift/false) removes `responder` from the list of monitored objects.

## Parameters

- `visible`: A Boolean value that indicates whether to make the palette visible when   becomes active. Specify   to show the palette when the object becomes the first responder.
- `responder`: A responder object associated with the tool picker’s window. Typically, you specify a view capable of becoming the first responder.

## See Also

- [var isVisible: Bool](pktoolpicker/isvisible.md)
  A Boolean value that indicates whether the tool picker is currently visible.
- [func frameObscured(in: UIView) -> CGRect](pktoolpicker/frameobscured(in:).md)
  Returns the portion of the specified view that the tool picker obscures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/setvisible(_:forfirstresponder:))*