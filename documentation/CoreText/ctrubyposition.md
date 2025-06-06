# CTRubyPosition

**Framework**: Core Text  
**Kind**: enum

Constants that specify the position of the ruby text relative to to the base text.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CTRubyPosition
```

## Topics

### Constants
- [CTRubyPosition.before](ctrubyposition/before.md)
  The ruby text is positioned before the base text, appearing above horizontal text and to the right of vertical text.
- [CTRubyPosition.after](ctrubyposition/after.md)
  The ruby text is positioned after the base text, appearing below horizontal text and to the left of vertical text.
- [CTRubyPosition.interCharacter](ctrubyposition/intercharacter.md)
  The ruby text is positioned to the right of the base text, regardless of whether it’s horizontal or vertical.
- [CTRubyPosition.inline](ctrubyposition/inline.md)
  The ruby text follows the base text with no special styling.
- [CTRubyPosition.count](ctrubyposition/count.md)
  A constant that accounts for all ruby positions during ruby annotation creation.
### Initializers
- [init?(rawValue: UInt8)](ctrubyposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md)
  Constants that track the progress of font descriptor matching.
- [enum CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md)
  Sets the auto-activation for the specified bundle identifier.
- [enum CTFontManagerError](ctfontmanagererror.md)
  Errors that prevent unregistration of fonts for a specified font file URL.
- [enum CTFontManagerScope](ctfontmanagerscope.md)
  Constants that define the scope for font registration.
- [struct CTLineBoundsOptions](ctlineboundsoptions.md)
  Options for getting the bounds of a line of text.
- [enum CTRubyAlignment](ctrubyalignment.md)
  Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [enum CTRubyOverhang](ctrubyoverhang.md)
  Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyposition)*