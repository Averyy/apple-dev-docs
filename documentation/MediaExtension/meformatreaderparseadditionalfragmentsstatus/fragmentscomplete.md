# fragmentsComplete

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Type Property

Indicates that the format reader can’t receive any more fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var fragmentsComplete: MEFormatReaderParseAdditionalFragmentsStatus { get }
```

```c
MEFormatReaderParseAdditionalFragmentsStatusFragmentsComplete
```

#### Discussion

Additional calls of [`parseAdditionalFragments(completionHandler:)`](../meformatreader/parseadditionalfragments%28completionhandler%29.md) return an error.

## See Also

### Evaluating a fragment parsing operation
- [static var sizeIncreased: MEFormatReaderParseAdditionalFragmentsStatus](./sizeincreased.md)
  Indicates that the format reader file size increased.
- [static var fragmentAdded: MEFormatReaderParseAdditionalFragmentsStatus](./fragmentadded.md)
  Indicates that the format reader received one or more fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderparseadditionalfragmentsstatus/fragmentscomplete)*