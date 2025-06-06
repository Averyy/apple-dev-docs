# CTFontCollectionCreateFromAvailableFonts(_:)

**Framework**: Core Text  
**Kind**: func

Returns a new font collection containing all available fonts.

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
func CTFontCollectionCreateFromAvailableFonts(_ options: CFDictionary?) -> CTFontCollection
```

#### Return Value

A new collection containing all fonts available to the current application.

## Parameters

- `options`: The options dictionary. For possible values, see Constants.

## See Also

- [func CTFontCollectionCreateWithFontDescriptors(CFArray?, CFDictionary?) -> CTFontCollection](ctfontcollectioncreatewithfontdescriptors(_:_:).md)
  Returns a new font collection based on the given array of font descriptors.
- [func CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection, CFArray?, CFDictionary?) -> CTFontCollection](ctfontcollectioncreatecopywithfontdescriptors(_:_:_:).md)
  Returns a copy of the original collection augmented with the given new font descriptors.
- [func CTFontCollectionCreateMutableCopy(CTFontCollection) -> CTMutableFontCollection](ctfontcollectioncreatemutablecopy(_:).md)
  Creates a mutable copy of the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncreatefromavailablefonts(_:))*