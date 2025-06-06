# CTFontCollectionCopyQueryDescriptors(_:)

**Framework**: Core Text  
**Kind**: func

Retrieves the array of descriptors for font matching.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCopyQueryDescriptors(_ collection: CTFontCollection) -> CFArray?
```

#### Return Value

A retained reference to the array of descriptors for querying (matching) the system font database. The return value is undefined if you create the collection with [`CTFontCollectionCreateFromAvailableFonts(_:)`](ctfontcollectioncreatefromavailablefonts(_:).md).

## Parameters

- `collection`: The font collection reference.

## See Also

- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyexclusiondescriptors(_:).md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetexclusiondescriptors(_:_:).md)
  Replaces the array of descriptors to exclude from the match.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetquerydescriptors(_:_:).md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyquerydescriptors(_:))*