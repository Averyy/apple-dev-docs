# kCGImageMetadataEnumerateRecursively

**Framework**: Image I/O  
**Kind**: var

An option to enumerate recursively through a set of metadata tags.

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
let kCGImageMetadataEnumerateRecursively: CFString
```

#### Discussion

The value of this key is a [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). Set the value to [`kOSBooleanTrue`](https://developer.apple.com/documentation/DriverKit/kOSBooleanTrue) to enumerate all tags recursively. Set the value to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) to enumerate only the direct children of the root path you specify.

When you call [`CGImageMetadataEnumerateTagsUsingBlock(_:_:_:_:)`](cgimagemetadataenumeratetagsusingblock(_:_:_:_:).md), include this option if you want the enumeration behavior to search recursively through the available tags. If you don’t specify this key, the function behaves as if the value is false.

## See Also

- [func CGImageMetadataEnumerateTagsUsingBlock(CGImageMetadata, CFString?, CFDictionary?, CGImageMetadataTagBlock)](cgimagemetadataenumeratetagsusingblock(_:_:_:_:).md)
  Enumerates the tags of a metadata object and executes the specified block on each tag.
- [typealias CGImageMetadataTagBlock](cgimagemetadatatagblock.md)
  The block to execute when enumerating the tags of a metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagemetadataenumeraterecursively)*