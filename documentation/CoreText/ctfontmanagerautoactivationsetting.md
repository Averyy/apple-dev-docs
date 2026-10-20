# CTFontManagerAutoActivationSetting

**Framework**: Core Text  
**Kind**: enum  
**Role**: Enumeration

Sets the auto-activation for the specified bundle identifier.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CTFontManagerAutoActivationSetting
```

```c
enum CTFontManagerAutoActivationSetting : uint32_t;
```

## Topics

### Constants
- [CTFontManagerAutoActivationSetting.default](./ctfontmanagerautoactivationsetting/default.md)
- [CTFontManagerAutoActivationSetting.disabled](./ctfontmanagerautoactivationsetting/disabled.md)
- [CTFontManagerAutoActivationSetting.enabled](./ctfontmanagerautoactivationsetting/enabled.md)
- [CTFontManagerAutoActivationSetting.promptUser](./ctfontmanagerautoactivationsetting/promptuser.md)
### Initializers
- [init?(rawValue: UInt32)](./ctfontmanagerautoactivationsetting/init%28rawvalue%29.md)

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
- [enum CTFontManagerError](./ctfontmanagererror.md)
  Errors that prevent unregistration of fonts for a specified font file URL.
- [enum CTFontManagerScope](./ctfontmanagerscope.md)
  Constants that define the scope for font registration.
- [struct CTLineBoundsOptions](./ctlineboundsoptions.md)
  Options for getting the bounds of a line of text.
- [enum CTRubyAlignment](./ctrubyalignment.md)
  Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [enum CTRubyOverhang](./ctrubyoverhang.md)
  Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [enum CTRubyPosition](./ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting)*