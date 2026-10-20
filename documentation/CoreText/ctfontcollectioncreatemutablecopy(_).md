# CTFontCollectionCreateMutableCopy(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates a mutable copy of the original collection.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCreateMutableCopy(_ original: CTFontCollection) -> CTMutableFontCollection
```

```c
extern CTMutableFontCollectionRefCTFontCollectionCreateMutableCopy(CTFontCollectionRef original);
```

#### Return Value

A mutable copy of the original font collection.

## Parameters

- `original`: The original font collection reference.

## See Also

### Creating Font Collections
- [func CTFontCollectionCreateFromAvailableFonts(CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatefromavailablefonts%28_%29.md)
  Returns a new font collection containing all available fonts.
- [func CTFontCollectionCreateWithFontDescriptors(CFArray?, CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatewithfontdescriptors%28_,_%29.md)
  Returns a new font collection based on the given array of font descriptors.
- [func CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection, CFArray?, CFDictionary?) -> CTFontCollection](./ctfontcollectioncreatecopywithfontdescriptors%28_,_,_%29.md)
  Returns a copy of the original collection augmented with the given new font descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatemutablecopy(_:))*