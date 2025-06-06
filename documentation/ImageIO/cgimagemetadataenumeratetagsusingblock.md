# CGImageMetadataEnumerateTagsUsingBlock(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Enumerates the tags of a metadata object and executes the specified block on each tag.

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
func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: @escaping CGImageMetadataTagBlock)
```

#### Discussion

This function iterates over the tags in the specified metadata object. By default, it iterates over only the top-level tags. Include the [`kCGImageMetadataEnumerateRecursively`](kcgimagemetadataenumeraterecursively.md) constant in the `options` parameter to iterate over all tags recursively.

You must not modify the tag information from your block. Instead, use your block only to read information from the tags. If you need to modify any tags, add those tags to a collection object and modify them after this function finishes its enumeration.

## Parameters

- `metadata`: The metadata object that contains the tags to enumerate.
- `rootPath`: Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.
- `options`: A dictionary of additional options. Currently, the only supported option is  .
- `block`: The block to execute for each tag. For more information, see  .

## See Also

- [typealias CGImageMetadataTagBlock](cgimagemetadatatagblock.md)
  The block to execute when enumerating the tags of a metadata object.
- [let kCGImageMetadataEnumerateRecursively: CFString](kcgimagemetadataenumeraterecursively.md)
  An option to enumerate recursively through a set of metadata tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadataenumeratetagsusingblock(_:_:_:_:))*