# CTFontCollectionSortDescriptorsCallback

**Framework**: Core Text  
**Kind**: typealias

The collection sorting callback type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutableRawPointer) -> CFComparisonResult
```

#### Return Value

The matching font descriptors of a collection in sorted order.

## Parameters

- `first`: The first descriptor.
- `second`: The second descriptor.
- `refCon`: A pointer to contextual data from the client.

## See Also

- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncreatematchingfontdescriptors(_:).md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:).md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:).md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:).md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsortdescriptorscallback)*