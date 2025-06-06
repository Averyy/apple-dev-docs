# CTFontCollectionSetExclusionDescriptors(_:_:)

**Framework**: Core Text  
**Kind**: func

Replaces the array of descriptors to exclude from the match.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionSetExclusionDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

## Parameters

- `collection`: The font collection reference.
- `descriptors`: An array of   objects. This parameter can be  .

## See Also

- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyexclusiondescriptors(_:).md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncopyquerydescriptors(_:).md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](ctfontcollectionsetquerydescriptors(_:_:).md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsetexclusiondescriptors(_:_:))*