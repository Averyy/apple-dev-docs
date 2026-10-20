# textInputView

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An affiliated view that provides a coordinate system for all geometric values in this protocol.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var textInputView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * textInputView;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)
- [Supporting extended text interactions](../support-extended-text-interactions.md)

## See Also

### Managing the text input view
- [var unscaledView: UIView](./unscaledview.md)
  A view that represents the web content that’s agnostic of zoom state.
- [var selectionClipRect: CGRect](./selectioncliprect.md)
  A rectangle that represents the bounds of editable elements.
- [var unobscuredContentRect: CGRect](./unobscuredcontentrect.md)
  A rectangle that frames a user interface, such as text-selection handles, in an unobscured location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textinputview)*