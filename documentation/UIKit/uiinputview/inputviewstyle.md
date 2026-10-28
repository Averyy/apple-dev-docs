# inputViewStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style for the content of the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var inputViewStyle: UIInputView.Style { get }
```

```objc
@property (nonatomic, readonly) UIInputViewStyle inputViewStyle;
```

## Discussion

The style applies both to the current view and to any subviews that adopt the [`UIAppearance`](../uiappearance.md) protocol, which includes all standard system views.

## See Also

### Getting the input style
- [UIInputView.Style](./style.md)
  Constants that indicate the appearance changes for an input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview/inputviewstyle)*