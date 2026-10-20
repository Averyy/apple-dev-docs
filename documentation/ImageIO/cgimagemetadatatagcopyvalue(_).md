# CGImageMetadataTagCopyValue(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern CFTypeRefCGImageMetadataTagCopyValue(CGImageMetadataTagRef tag);
```

#### Return Value

A copy of the tag’s value. Possible return types are [`CFString`](../CoreFoundation/cfstring.md), [`CFNumber`](../CoreFoundation/cfnumber.md), [`CFBoolean`](../CoreFoundation/cfboolean.md), [`CFArray`](../CoreFoundation/cfarray.md), and [`CFDictionary`](../CoreFoundation/cfdictionary.md).

#### Discussion

Use this method to obtain the value when you want to use or display that value elsewhere. Any changes you make to the returned value don’t change the contents of the metadata tag. To change the value, call [`CGImageMetadataSetValueWithPath(_:_:_:_:)`](./cgimagemetadatasetvaluewithpath%28_,_,_,_%29.md) or [`CGImageMetadataSetTagWithPath(_:_:_:_:)`](./cgimagemetadatasettagwithpath%28_,_,_,_%29.md) instead.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

### Getting the Attributes of the Tag
- [func CGImageMetadataTagCopyNamespace(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopynamespace%28_%29.md)
  Returns an immutable copy of the tag’s XMP namespace.
- [func CGImageMetadataTagCopyPrefix(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopyprefix%28_%29.md)
  Returns an immutable copy of the tag’s prefix.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopyname%28_%29.md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyQualifiers(CGImageMetadataTag) -> CFArray?](./cgimagemetadatatagcopyqualifiers%28_%29.md)
  Returns a shallow copy of the metadata tags that act as qualifiers for the current tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopyvalue(_:))*