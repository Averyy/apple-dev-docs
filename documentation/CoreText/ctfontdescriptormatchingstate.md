# CTFontDescriptorMatchingState

**Framework**: Core Text  
**Kind**: enum

Constants that track the progress of font descriptor matching.

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
enum CTFontDescriptorMatchingState
```

## Topics

### Constants
- [CTFontDescriptorMatchingState.didBegin](ctfontdescriptormatchingstate/didbegin.md)
  A state that indicates matching is about to begin.
- [CTFontDescriptorMatchingState.didFinish](ctfontdescriptormatchingstate/didfinish.md)
  A state that indicates matching is done.
- [CTFontDescriptorMatchingState.willBeginQuerying](ctfontdescriptormatchingstate/willbeginquerying.md)
  A state that indicates communication with the server is about to begin.
- [CTFontDescriptorMatchingState.stalled](ctfontdescriptormatchingstate/stalled.md)
  A state that indicates that matching is stalled, such as while waiting for a server response.
- [CTFontDescriptorMatchingState.willBeginDownloading](ctfontdescriptormatchingstate/willbegindownloading.md)
  A state that indicates downloading is about to begin.
- [CTFontDescriptorMatchingState.downloading](ctfontdescriptormatchingstate/downloading.md)
  A state that indicates downloading is in progress.
- [CTFontDescriptorMatchingState.didFinishDownloading](ctfontdescriptormatchingstate/didfinishdownloading.md)
  A state that indicates downloading is done.
- [CTFontDescriptorMatchingState.didMatch](ctfontdescriptormatchingstate/didmatch.md)
  A state that indicates the font descriptor match is successful.
- [CTFontDescriptorMatchingState.didFailWithError](ctfontdescriptormatchingstate/didfailwitherror.md)
  A state that indicates an error.
### Initializers
- [init?(rawValue: UInt32)](ctfontdescriptormatchingstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [enum CTRubyPosition](ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)*