# unobscuredContentRect

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

A rectangle that frames a user interface, such as text-selection handles, in an unobscured location.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var unobscuredContentRect: CGRect { get }
```

#### Discussion

Return a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) instance configured in the coordinate space of [`textInputView`](betextinput/textinputview.md).

## See Also

- [var textInputView: UIView](betextinput/textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var unscaledView: UIView](betextinput/unscaledview.md)
  A view that represents the web content that’s agnostic of zoom state.
- [var selectionClipRect: CGRect](betextinput/selectioncliprect.md)
  A rectangle that represents the bounds of editable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/unobscuredcontentrect)*