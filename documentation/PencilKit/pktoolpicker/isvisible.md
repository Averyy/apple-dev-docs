# isVisible

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the tool picker is currently visible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isVisible;
```

## See Also

### Coordinating the visibility of the picker
- [func setVisible(Bool, forFirstResponder: UIResponder)](./setvisible%28_,forfirstresponder%29.md)
  Sets the visibility for the tool picker, based on when the specified responder object becomes active.
- [func frameObscured(in: UIView) -> CGRect](./frameobscured%28in%29.md)
  Returns the portion of the specified view that the tool picker obscures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/isvisible)*