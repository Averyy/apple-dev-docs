# CTFontCollectionSetQueryDescriptors(_:_:)

**Framework**: Core Text  
**Kind**: func

Replaces the array of descriptors for font matching.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionSetQueryDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

## Parameters

- `collection`: The font collection reference.
- `descriptors`: An array of   objects. Passing in   represents an empty collection, which sets the matching descriptors to  .

## See Also

- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyexclusiondescriptors(_:).md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyquerydescriptors(_:).md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetexclusiondescriptors(_:_:).md)
  Replaces the array of descriptors to exclude from the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsetquerydescriptors(_:_:))*