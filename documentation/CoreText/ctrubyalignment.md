# CTRubyAlignment

**Framework**: Core Text  
**Kind**: enum

Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.

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
enum CTRubyAlignment
```

## Topics

### Constants
- [CTRubyAlignment.auto](ctrubyalignment/auto.md)
  Core Text automatically determines the alignment.
- [CTRubyAlignment.start](ctrubyalignment/start.md)
  Aligns the ruby text with the starting edge of the base text.
- [CTRubyAlignment.center](ctrubyalignment/center.md)
  Centers the ruby text within the width of the base text.
- [CTRubyAlignment.end](ctrubyalignment/end.md)
  Aligns the ruby text with the ending edge of the base text.
- [CTRubyAlignment.distributeLetter](ctrubyalignment/distributeletter.md)
  Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [CTRubyAlignment.distributeSpace](ctrubyalignment/distributespace.md)
  Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [CTRubyAlignment.lineEdge](ctrubyalignment/lineedge.md)
  Aligns the ruby text to an adjacent line edge.
- [CTRubyAlignment.invalid](ctrubyalignment/invalid.md)
  The alignment is invalid.
### Initializers
- [init?(rawValue: UInt8)](ctrubyalignment/init(rawvalue:).md)

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
- [enum CTRubyOverhang](ctrubyoverhang.md)
  Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [enum CTRubyPosition](ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyalignment)*