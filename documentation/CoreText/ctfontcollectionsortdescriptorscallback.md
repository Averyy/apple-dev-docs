# CTFontCollectionSortDescriptorsCallback

**Framework**: Core Text  
**Kind**: typealias  
**Role**: Type Alias

The collection sorting callback type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutableRawPointer) -> CFComparisonResult
```

```c
typedef enum CFComparisonResult (*)(const struct __CTFontDescriptor *, const struct __CTFontDescriptor *, void *) CTFontCollectionSortDescriptorsCallback;
```

## Return Value

The matching font descriptors of a collection in sorted order.

## Parameters

- `first`: The first descriptor.
- `second`: The second descriptor.
- `refCon`: A pointer to contextual data from the client.

## See Also

### Getting Font Descriptors
- [func CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptors%28_%29.md)
  Returns an array of font descriptors matching the collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorswithoptions%28_,_%29.md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorssortedwithcallback%28_,_,_%29.md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorsforfamily%28_,_,_%29.md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectionsortdescriptorscallback)*