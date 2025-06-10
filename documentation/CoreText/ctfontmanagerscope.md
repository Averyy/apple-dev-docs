# CTFontManagerScope

**Framework**: Core Text  
**Kind**: enum

Constants that define the scope for font registration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTFontManagerScope
```

#### Overview

On macOS, a user session refers to a login session. On iOS, a user session refers to the current booted session.

## Topics

### Constants
- [CTFontManagerScope.none](ctfontmanagerscope/none.md)
  No scope is defined.
- [CTFontManagerScope.process](ctfontmanagerscope/process.md)
  The font is available to the current process for the duration of the process unless directly unregistered.
- [CTFontManagerScope.persistent](ctfontmanagerscope/persistent.md)
  The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [CTFontManagerScope.session](ctfontmanagerscope/session.md)
  The font is available to the current user session but won’t be available in subsequent sessions.
- [static var user: CTFontManagerScope](ctfontmanagerscope/user.md)
  The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
### Initializers
- [init?(rawValue: UInt32)](ctfontmanagerscope/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md)
  Constants that track the progress of font descriptor matching.
- [enum CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md)
  Sets the auto-activation for the specified bundle identifier.
- [enum CTFontManagerError](ctfontmanagererror.md)
  Errors that prevent unregistration of fonts for a specified font file URL.
- [struct CTLineBoundsOptions](ctlineboundsoptions.md)
  Options for getting the bounds of a line of text.
- [enum CTRubyAlignment](ctrubyalignment.md)
  Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [enum CTRubyOverhang](ctrubyoverhang.md)
  Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [enum CTRubyPosition](ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerscope)*