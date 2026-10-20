# tooManyAssetLocalesAllocated

**Framework**: Speech  
**Kind**: property  
**Role**: Type Property

The application has allocated too many locales.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var tooManyAssetLocalesAllocated: SFSpeechError.Code { get }
```

## See Also

### Asset errors
- [static var assetLocaleNotAllocated: SFSpeechError.Code](./assetlocalenotallocated.md)
  The asset locale has not been allocated, but module requires it.
- [static var cannotAllocateUnsupportedLocale: SFSpeechError.Code](./cannotallocateunsupportedlocale.md)
  The asset locale being requested is not supported by SpeechFramework.
- [static var noModel: SFSpeechError.Code](./nomodel.md)
  The selected locale/options does not have an appropriate model available or downloadable.
- [SFSpeechError.Code.timeout](./timeout.md)
  The operation timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeecherror/code/toomanyassetlocalesallocated)*