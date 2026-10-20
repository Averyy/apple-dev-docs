# CTRubyOverhang

**Framework**: Core Text  
**Kind**: enum  
**Role**: Enumeration

Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.

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
enum CTRubyOverhang
```

```c
enum CTRubyOverhang : uint8_t;
```

## Topics

### Constants
- [CTRubyOverhang.auto](./ctrubyoverhang/auto.md)
  The ruby text can overhang adjacent text on both sides.
- [CTRubyOverhang.start](./ctrubyoverhang/start.md)
  The ruby text can overhang the text that precedes it.
- [CTRubyOverhang.end](./ctrubyoverhang/end.md)
  The ruby text can overhang the text that follows it.
- [CTRubyOverhang.none](./ctrubyoverhang/none.md)
  The ruby text can’t overhang the preceding or following text.
- [CTRubyOverhang.invalid](./ctrubyoverhang/invalid.md)
  The overhang specification is invalid.
### Initializers
- [init?(rawValue: UInt8)](./ctrubyoverhang/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum CTFontDescriptorMatchingState](./ctfontdescriptormatchingstate.md)
  Constants that track the progress of font descriptor matching.
- [enum CTFontManagerAutoActivationSetting](./ctfontmanagerautoactivationsetting.md)
  Sets the auto-activation for the specified bundle identifier.
- [enum CTFontManagerError](./ctfontmanagererror.md)
  Errors that prevent unregistration of fonts for a specified font file URL.
- [enum CTFontManagerScope](./ctfontmanagerscope.md)
  Constants that define the scope for font registration.
- [struct CTLineBoundsOptions](./ctlineboundsoptions.md)
  Options for getting the bounds of a line of text.
- [enum CTRubyAlignment](./ctrubyalignment.md)
  Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [enum CTRubyPosition](./ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyoverhang)*