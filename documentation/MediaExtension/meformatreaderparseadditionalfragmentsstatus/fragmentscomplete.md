# fragmentsComplete

**Framework**: MediaExtension  
**Kind**: property

Indicates that the format reader can’t receive any more fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var fragmentsComplete: MEFormatReaderParseAdditionalFragmentsStatus { get }
```

#### Discussion

Additional calls of [`parseAdditionalFragments(completionHandler:)`](meformatreader/parseadditionalfragments(completionhandler:).md) return an error.

## See Also

- [static var sizeIncreased: MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus/sizeincreased.md)
  Indicates that the format reader file size increased.
- [static var fragmentAdded: MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus/fragmentadded.md)
  Indicates that the format reader received one or more fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderparseadditionalfragmentsstatus/fragmentscomplete)*