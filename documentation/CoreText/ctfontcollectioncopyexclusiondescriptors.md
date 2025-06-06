# CTFontCollectionCopyExclusionDescriptors(_:)

**Framework**: Core Text  
**Kind**: func

Retrieves the array of descriptors to exclude from the match.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCopyExclusionDescriptors(_ collection: CTFontCollection) -> CFArray?
```

#### Return Value

A retained reference to the array of descriptors for querying (matching) the system font database.

## Parameters

- `collection`: The font collection reference.

## See Also

- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyquerydescriptors(_:).md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetexclusiondescriptors(_:_:).md)
  Replaces the array of descriptors to exclude from the match.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetquerydescriptors(_:_:).md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyexclusiondescriptors(_:))*