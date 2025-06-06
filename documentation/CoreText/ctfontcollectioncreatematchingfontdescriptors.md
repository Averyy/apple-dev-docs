# CTFontCollectionCreateMatchingFontDescriptors(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of font descriptors matching the collection.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCollectionCreateMatchingFontDescriptors(_ collection: CTFontCollection) -> CFArray?
```

#### Return Value

A retained reference to an array of normalized font descriptors matching the collection definition.

## Parameters

- `collection`: The font collection reference.

## See Also

- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:).md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:).md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:).md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptors(_:))*