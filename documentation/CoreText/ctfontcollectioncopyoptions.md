# CTFontCollectionCopyOptions

**Framework**: Core Text  
**Kind**: struct

Option bits for use with CTFontCollectionCopyFontAttribute(s).

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
struct CTFontCollectionCopyOptions
```

## Topics

### Constants
- [static var standardSort: CTFontCollectionCopyOptions](ctfontcollectioncopyoptions/standardsort.md)
  Passing this option indicates that the return values should be sorted in standard UI order, suitable for display to the user. This is the same sorting behavior used by `NSFontPanel` and Font Book.
- [static var unique: CTFontCollectionCopyOptions](ctfontcollectioncopyoptions/unique.md)
  Passing this option indicates that duplicate values should be removed from the results.
### Initializers
- [init(rawValue: UInt32)](ctfontcollectioncopyoptions/init(rawvalue:).md)
  Creates a copy options structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [let kCTFontCollectionRemoveDuplicatesOption: CFString](kctfontcollectionremoveduplicatesoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions)*