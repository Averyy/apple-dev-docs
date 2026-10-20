# UIInputView.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the appearance changes for an input view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum UIInputViewStyle : NSInteger;
```

## Topics

### Constants
- [UIInputView.Style.default](./style/default.md)
  Apply blur behaviors to the view so that it looks like it belongs with the keyboard.
- [UIInputView.Style.keyboard](./style/keyboard.md)
  Apply both blur and tinting effects to the view to mimic the keyboard background.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the input style
- [var inputViewStyle: UIInputView.Style](./inputviewstyle.md)
  The style for the content of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview/style)*