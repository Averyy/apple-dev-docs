# CTFontCollectionCreateMatchingFontDescriptors(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFArrayRefCTFontCollectionCreateMatchingFontDescriptors(CTFontCollectionRef collection);
```

#### Return Value

A retained reference to an array of normalized font descriptors matching the collection definition.

## Parameters

- `collection`: The font collection reference.

## See Also

### Getting Font Descriptors
- [func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorswithoptions%28_,_%29.md)
  Creates an array of font descriptors that match the specified collection.
- [func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection, CTFontCollectionSortDescriptorsCallback?, UnsafeMutableRawPointer?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorssortedwithcallback%28_,_,_%29.md)
  Returns the array of matching font descriptors sorted with the callback function.
- [func CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection, CFString, CFDictionary?) -> CFArray?](./ctfontcollectioncreatematchingfontdescriptorsforfamily%28_,_,_%29.md)
  Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [typealias CTFontCollectionSortDescriptorsCallback](./ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptors(_:))*