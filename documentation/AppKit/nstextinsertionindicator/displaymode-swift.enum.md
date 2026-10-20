# NSTextInsertionIndicator.DisplayMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine how to display the system text cursor in a custom text UI.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum DisplayMode
```

```c
enum NSTextInsertionIndicatorDisplayMode : NSInteger;
```

## Topics

### Defining the display mode
- [NSTextInsertionIndicator.DisplayMode.automatic](./displaymode-swift.enum/automatic.md)
- [NSTextInsertionIndicator.DisplayMode.hidden](./displaymode-swift.enum/hidden.md)
- [NSTextInsertionIndicator.DisplayMode.visible](./displaymode-swift.enum/visible.md)
### Initializers
- [init?(rawValue: Int)](./displaymode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Text input
- [Adopting the system text cursor in custom text views](../adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](../nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](../nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](../nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](../nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](../nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.AutomaticModeOptions](./automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/displaymode-swift.enum)*