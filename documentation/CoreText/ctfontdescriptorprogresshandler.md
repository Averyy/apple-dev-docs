# CTFontDescriptorProgressHandler

**Framework**: Core Text  
**Kind**: typealias

The progress callback type.

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
typealias CTFontDescriptorProgressHandler = (CTFontDescriptorMatchingState, CFDictionary) -> Bool
```

#### Discussion

Use this callback type with [`CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)`](ctfontdescriptormatchfontdescriptorswithprogresshandler(_:_:_:).md).

## See Also

- [typealias ATSFontRef](atsfontref.md)
- [typealias CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler)*