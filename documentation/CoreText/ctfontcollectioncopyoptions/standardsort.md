# standardSort

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

Passing this option indicates that the return values should be sorted in standard UI order, suitable for display to the user. This is the same sorting behavior used by `NSFontPanel` and Font Book.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var standardSort: CTFontCollectionCopyOptions { get }
```

```c
kCTFontCollectionCopyStandardSort
```

## See Also

### Constants
- [static var unique: CTFontCollectionCopyOptions](./unique.md)
  Passing this option indicates that duplicate values should be removed from the results.
- [kCTFontCollectionCopyDefaultOptions](./kctfontcollectioncopydefaultoptions.md)
  Passing this option indicates that defaults are to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/standardsort)*