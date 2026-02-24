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
- `rootPath`: A string that contains the path to the root tag. Specify `NULL` to enumerate the top-level tags in the metadata object. A path consists of the tag’s name, plus optional prefix and parent information. Separate prefix information from other path information using a colon (`:`) character. Separate parent and child tags using the period (`.`) character. For example, the string `“exif:Flash.RedEyeMode”` represents the path to the `RedEyeMode` field of the `Flash` parent structure in the EXIF metadata. When a tag contains an ordered or unordered array, specify elements using a `0`-based index inside square brackets. For example, use the string `“dc.subject[2]”` to access the third element in the `subject` array. When the tag contains an alternate-text array, access elements using an RFC 3066 language code inside square brackets. For example, use the string `“dc.description[de]”` to access the German description information. Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.
- `options`: A dictionary of additional options. Currently, the only supported option is [`kCGImageMetadataEnumerateRecursively`](kcgimagemetadataenumeraterecursively.md).
- `block`: The block to execute for each tag. For more information, see [`CGImageMetadataTagBlock`](cgimagemetadatatagblock.md).

## See Also

- [typealias CGImageMetadataTagBlock](cgimagemetadatatagblock.md)
  The block to execute when enumerating the tags of a metadata object.
- [let kCGImageMetadataEnumerateRecursively: CFString](kcgimagemetadataenumeraterecursively.md)
  An option to enumerate recursively through a set of metadata tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadataenumeratetagsusingblock(_:_:_:_:))*