# CGImageMetadataTagCopyValue(_:)

**Framework**: Image I/O  
**Kind**: func

Returns a shallow copy of the tag’s value, which is suitable only for reading.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag) -> CFTypeRef?
```

#### Return Value

A copy of the tag’s value. Possible return types are [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString), [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber), [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean), [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray), and [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary).

#### Discussion

Use this method to obtain the value when you want to use or display that value elsewhere. Any changes you make to the returned value don’t change the contents of the metadata tag. To change the value, call [`CGImageMetadataSetValueWithPath(_:_:_:_:)`](cgimagemetadatasetvaluewithpath(_:_:_:_:).md) or [`CGImageMetadataSetTagWithPath(_:_:_:_:)`](cgimagemetadatasettagwithpath(_:_:_:_:).md) instead.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

- [func CGImageMetadataTagCopyNamespace(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopynamespace(_:).md)
  Returns an immutable copy of the tag’s XMP namespace.
- [func CGImageMetadataTagCopyPrefix(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyprefix(_:).md)
  Returns an immutable copy of the tag’s prefix.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyname(_:).md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyQualifiers(CGImageMetadataTag) -> CFArray?](cgimagemetadatatagcopyqualifiers(_:).md)
  Returns a shallow copy of the metadata tags that act as qualifiers for the current tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopyvalue(_:))*