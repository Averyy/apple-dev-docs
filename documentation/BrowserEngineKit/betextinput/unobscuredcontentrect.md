# unobscuredContentRect

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly) CGRect unobscuredContentRect;
```

## Discussion

Return a [`CGRect`](../../CoreFoundation/cgrect.md) instance configured in the coordinate space of [`textInputView`](./textinputview.md).

## See Also

### Managing the text input view
- [var textInputView: UIView](./textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var unscaledView: UIView](./unscaledview.md)
  A view that represents the web content that’s agnostic of zoom state.
- [var selectionClipRect: CGRect](./selectioncliprect.md)
  A rectangle that represents the bounds of editable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/unobscuredcontentrect)*