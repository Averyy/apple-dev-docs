# NSTextInsertionIndicator.AutomaticModeOptions

**Framework**: AppKit  
**Kind**: struct

Options that affect the automatic display mode.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct AutomaticModeOptions
```

## Topics

### Configuring automatic mode options
- [static var showEffectsView: NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct/showeffectsview.md)
  Specifies whether a trailing glow displays during dictation.
- [static var showWhileTracking: NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct/showwhiletracking.md)
  Specifies whether the insertion indicator shows during a tracking loop.
### Initializers
- [init(rawValue: Int)](nstextinsertionindicator/automaticmodeoptions-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/automaticmodeoptions-swift.struct)*