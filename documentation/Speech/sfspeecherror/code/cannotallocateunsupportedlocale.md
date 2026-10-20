# cannotAllocateUnsupportedLocale

**Framework**: Speech  
**Kind**: property  
**Role**: Type Property

The asset locale being requested is not supported by SpeechFramework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var cannotAllocateUnsupportedLocale: SFSpeechError.Code { get }
```

## See Also

### Asset errors
- [static var assetLocaleNotAllocated: SFSpeechError.Code](./assetlocalenotallocated.md)
  The asset locale has not been allocated, but module requires it.
- [static var noModel: SFSpeechError.Code](./nomodel.md)
  The selected locale/options does not have an appropriate model available or downloadable.
- [SFSpeechError.Code.timeout](./timeout.md)
  The operation timed out.
- [static var tooManyAssetLocalesAllocated: SFSpeechError.Code](./toomanyassetlocalesallocated.md)
  The application has allocated too many locales.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeecherror/code/cannotallocateunsupportedlocale)*