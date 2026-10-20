# CTFontDescriptorProgressHandler

**Framework**: Core Text  
**Kind**: typealias  
**Role**: Type Alias

The progress callback type.

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
typealias CTFontDescriptorProgressHandler = (CTFontDescriptorMatchingState, CFDictionary) -> Bool
```

```c
typedef _Bool (^)(enum CTFontDescriptorMatchingState, const struct __CFDictionary *) CTFontDescriptorProgressHandler;
```

#### Discussion

Use this callback type with [`CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)`](./ctfontdescriptormatchfontdescriptorswithprogresshandler%28_,_,_%29.md).

## See Also

### Data Types
- [typealias ATSFontRef](./atsfontref.md)
- [typealias CTFontCollectionSortDescriptorsCallback](./ctfontcollectionsortdescriptorscallback.md)
  The collection sorting callback type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler)*