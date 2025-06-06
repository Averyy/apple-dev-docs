# CTFontCollectionCreateMutableCopy(_:)

**Framework**: Core Text  
**Kind**: func

Creates a mutable copy of the original collection.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCreateMutableCopy(_ original: CTFontCollection) -> CTMutableFontCollection
```

#### Return Value

A mutable copy of the original font collection.

## Parameters

- `original`: The original font collection reference.

## See Also

- [func CTFontCollectionCreateFromAvailableFonts(CFDictionary?) -> CTFontCollection](ctfontcollectioncreatefromavailablefonts(_:).md)
  Returns a new font collection containing all available fonts.
- [func CTFontCollectionCreateWithFontDescriptors(CFArray?, CFDictionary?) -> CTFontCollection](ctfontcollectioncreatewithfontdescriptors(_:_:).md)
  Returns a new font collection based on the given array of font descriptors.
- [func CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection, CFArray?, CFDictionary?) -> CTFontCollection](ctfontcollectioncreatecopywithfontdescriptors(_:_:_:).md)
  Returns a copy of the original collection augmented with the given new font descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatemutablecopy(_:))*