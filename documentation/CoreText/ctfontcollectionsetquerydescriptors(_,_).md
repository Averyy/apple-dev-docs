# CTFontCollectionSetQueryDescriptors(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Replaces the array of descriptors for font matching.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionSetQueryDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

```c
extern void CTFontCollectionSetQueryDescriptors(CTMutableFontCollectionRef collection, CFArrayRef descriptors);
```

## Parameters

- `collection`: The font collection reference.
- `descriptors`: An array of [`CTFontDescriptor`](./ctfontdescriptor.md) objects. Passing in `NULL` represents an empty collection, which sets the matching descriptors to `NULL`.

## See Also

### Excluding and Including Font Descriptors
- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyexclusiondescriptors%28_%29.md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyquerydescriptors%28_%29.md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetexclusiondescriptors%28_,_%29.md)
  Replaces the array of descriptors to exclude from the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsetquerydescriptors(_:_:))*