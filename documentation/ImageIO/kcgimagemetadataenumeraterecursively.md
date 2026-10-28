# kCGImageMetadataEnumerateRecursively

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kCGImageMetadataEnumerateRecursively;
```

## Discussion

The value of this key is a [`CFBoolean`](../CoreFoundation/cfboolean.md). Set the value to [`kOSBooleanTrue`](../DriverKit/kosbooleantrue.md) to enumerate all tags recursively. Set the value to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) to enumerate only the direct children of the root path you specify.

When you call [`CGImageMetadataEnumerateTagsUsingBlock(_:_:_:_:)`](./cgimagemetadataenumeratetagsusingblock%28_,_,_,_%29.md), include this option if you want the enumeration behavior to search recursively through the available tags. If you don’t specify this key, the function behaves as if the value is false.

## See Also

### Enumerating the Metadata Tags
- [func CGImageMetadataEnumerateTagsUsingBlock(CGImageMetadata, CFString?, CFDictionary?, CGImageMetadataTagBlock)](./cgimagemetadataenumeratetagsusingblock%28_,_,_,_%29.md)
  Enumerates the tags of a metadata object and executes the specified block on each tag.
- [typealias CGImageMetadataTagBlock](./cgimagemetadatatagblock.md)
  The block to execute when enumerating the tags of a metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagemetadataenumeraterecursively)*