# CPTextButtonStyle

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The styles a button can apply to its title to communicate its action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPTextButtonStyle
```

```c
enum CPTextButtonStyle : NSInteger;
```

## Topics

### Button Text Styles
- [CPTextButtonStyle.normal](./cptextbuttonstyle/normal.md)
  A style that indicates the button performs an action other than to confirm or cancel.
- [CPTextButtonStyle.confirm](./cptextbuttonstyle/confirm.md)
  A style that indicates the button confirms an action and changes data.
- [CPTextButtonStyle.cancel](./cptextbuttonstyle/cancel.md)
  A style that indicates the button cancels an action and doesn’t change data.
### Initializers
- [init?(rawValue: Int)](./cptextbuttonstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the Button Style
- [var textStyle: CPTextButtonStyle](./cptextbutton/textstyle.md)
  The text style the button applies to its title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptextbuttonstyle)*