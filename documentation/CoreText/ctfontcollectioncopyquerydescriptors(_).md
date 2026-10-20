# CTFontCollectionCopyQueryDescriptors(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Retrieves the array of descriptors for font matching.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCopyQueryDescriptors(_ collection: CTFontCollection) -> CFArray?
```

```c
extern CFArrayRefCTFontCollectionCopyQueryDescriptors(CTFontCollectionRef collection);
```

#### Return Value

A retained reference to the array of descriptors for querying (matching) the system font database. The return value is undefined if you create the collection with [`CTFontCollectionCreateFromAvailableFonts(_:)`](./ctfontcollectioncreatefromavailablefonts%28_%29.md).

## Parameters

- `collection`: The font collection reference.

## See Also

### Excluding and Including Font Descriptors
- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyexclusiondescriptors%28_%29.md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetexclusiondescriptors%28_,_%29.md)
  Replaces the array of descriptors to exclude from the match.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetquerydescriptors%28_,_%29.md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyquerydescriptors(_:))*