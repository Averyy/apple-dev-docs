# unscaledView

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A view that represents the web content that’s agnostic of zoom state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var unscaledView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * unscaledView;
```

#### Discussion

This property draws zoom-agnostic system user interface, such as text selection handles.

## See Also

### Managing the text input view
- [var textInputView: UIView](./textinputview.md)
  An affiliated view that provides a coordinate system for all geometric values in this protocol.
- [var selectionClipRect: CGRect](./selectioncliprect.md)
  A rectangle that represents the bounds of editable elements.
- [var unobscuredContentRect: CGRect](./unobscuredcontentrect.md)
  A rectangle that frames a user interface, such as text-selection handles, in an unobscured location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/unscaledview)*