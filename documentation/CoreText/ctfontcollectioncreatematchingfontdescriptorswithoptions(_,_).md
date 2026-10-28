# CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFArrayRefCTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollectionRef collection, CFDictionaryRef options);
```

## Return Value

An array of [`CTFontDescriptor`](./ctfontdescriptor.md) objects that match the collection definition, or `NULL` if there are none.

## Parameters

- `collection`: The font collection reference.
- `options`: The options dictionary. Passing in `NULL` returns the same results as calling [`CTFontCollectionCreateMatchingFontDescriptors(_:)`](./ctfontcollectioncreatematchingfontdescriptors%28_%29.md), which uses the options specified during the collection’s creation.

## See Also

### Getting Font Descriptors
- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptors%28_%29.md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorssortedwithcallback%28_,_,_%29.md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorsforfamily%28_,_,_%29.md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](./ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:))*