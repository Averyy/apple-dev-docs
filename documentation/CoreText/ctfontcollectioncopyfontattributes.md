# CTFontCollectionCopyFontAttributes(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Retrieves an array of dictionaries containing font descriptor attribute values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.7+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func CTFontCollectionCopyFontAttributes(_ collection: CTFontCollection, _ attributeNames: CFSet, _ options: CTFontCollectionCopyOptions) -> CFArray
```

#### Return Value

An array that contains one [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) value for each descriptor mapping the specified attribute names.

## Parameters

- `collection`: The font collection reference.
- `attributeNames`: The attributes to retrieve for each descriptor in the collection.
- `options`: Options to alter the return value. With  , the values appear in the same order as the results from  . Setting   removes duplicate values. Setting   sorts the values in standard UI order.

## See Also

- [func CTFontCollectionCopyFontAttribute(CTFontCollection, CFString, CTFontCollectionCopyOptions) -> CFArray](ctfontcollectioncopyfontattribute(_:_:_:).md)
  Retrieves an array of font descriptor attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyfontattributes(_:_:_:))*