# CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_:_:)

**Framework**: Core Text  
**Kind**: func

Creates an array of font descriptors that match the specified collection.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_ collection: CTFontCollection, _ options: CFDictionary?) -> CFArray?
```

#### Return Value

An array of [`CTFontDescriptor`](ctfontdescriptor.md) objects that match the collection definition, or `NULL` if there are none.

## Parameters

- `collection`: The font collection reference.
- `options`: The options dictionary. Passing in   returns the same results as calling  , which uses the options specified during the collection’s creation.

## See Also

- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncreatematchingfontdescriptors(_:).md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:).md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:).md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:))*