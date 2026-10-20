# CTFontCollectionSetExclusionDescriptors(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Replaces the array of descriptors to exclude from the match.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionSetExclusionDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

```c
extern void CTFontCollectionSetExclusionDescriptors(CTMutableFontCollectionRef collection, CFArrayRef descriptors);
```

## Parameters

- `collection`: The font collection reference.
- `descriptors`: An array of [`CTFontDescriptor`](./ctfontdescriptor.md) objects. This parameter can be `NULL`.

## See Also

### Excluding and Including Font Descriptors
- [func CTFontCollectionCopyExclusionDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyexclusiondescriptors%28_%29.md)
  Retrieves the array of descriptors to exclude from the match.
- [func CTFontCollectionCopyQueryDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncopyquerydescriptors%28_%29.md)
  Retrieves the array of descriptors for font matching.
- [func CTFontCollectionSetQueryDescriptors(CTMutableFontCollection, CFArray?)](./ctfontcollectionsetquerydescriptors%28_,_%29.md)
  Replaces the array of descriptors for font matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsetexclusiondescriptors(_:_:))*