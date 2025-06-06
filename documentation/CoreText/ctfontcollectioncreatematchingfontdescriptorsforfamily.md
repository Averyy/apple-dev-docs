# CTFontCollectionCreateMatchingFontDescriptorsForFamily(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CTFontCollectionCreateMatchingFontDescriptorsForFamily(_ collection: CTFontCollection, _ familyName: CFString, _ options: CFDictionary?) -> CFArray?
```

#### Return Value

An array of [`CTFontDescriptor`](ctfontdescriptor.md) objects that match the specified family in the collection, or `NULL` if there are none.

## Parameters

- `collection`: The font collection reference.
- `familyName`: The font family name.
- `options`: The options dictionary.

## See Also

- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncreatematchingfontdescriptors(_:).md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:).md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:).md)
  Returns the array of matching font descriptors sorted with the callback function.
- [typealias CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:))*