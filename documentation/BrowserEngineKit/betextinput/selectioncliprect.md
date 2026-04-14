# selectionClipRect

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

A rectangle that represents the bounds of editable elements.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var selectionClipRect: CGRect { get }
```

#### Discussion

This property ensures that the user interface doesn’t breach the specified area.

## See Also

- [var textInputView: UIView](betextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var unscaledView: UIView](betextinput/unscaledview.md)
  A view that represents the web content that’s agnostic of zoom state.
- [var unobscuredContentRect: CGRect](betextinput/unobscuredcontentrect.md)
  A rectangle that frames a user interface, such as text-selection handles, in an unobscured location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectioncliprect)*