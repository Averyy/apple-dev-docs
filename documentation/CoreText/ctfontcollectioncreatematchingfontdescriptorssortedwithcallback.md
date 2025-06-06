# CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns the array of matching font descriptors sorted with the callback function.

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
func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection, _ sortCallback: CTFontCollectionSortDescriptorsCallback?, _ refCon: UnsafeMutableRawPointer?) -> CFArray?
```

#### Return Value

An array of font descriptors matching the criteria of the collection sorted by the results of the sorting callback function.

## Parameters

- `collection`: The collection reference.
- `sortCallback`: The sorting callback function that defines the sort order.
- `refCon`: Pointer to client data define context for the callback.

## See Also

- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](ctfontcollectioncreatematchingfontdescriptors(_:).md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:).md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:).md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:))*