# CTFontCollectionCopyExclusionDescriptors(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Retrieves the array of descriptors to exclude from the match.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCopyExclusionDescriptors(_ collection: CTFontCollection) -> CFArray?
```

```c
extern CFArrayRefCTFontCollectionCopyExclusionDescriptors(CTFontCollectionRef collection);
```

#### Return Value

A retained reference to the array of descriptors for querying (matching) the system font database.

## Parameters

- `collection`: The font collection reference.

## See Also

### Excluding and Including Font Descriptors
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyquerydescriptors%28_%29.md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetexclusiondescriptors%28_,_%29.md)
  Replaces the array of descriptors to exclude from the match.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetquerydescriptors%28_,_%29.md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyexclusiondescriptors(_:))*