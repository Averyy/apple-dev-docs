# fileAttributes

**Framework**: Foundation  
**Kind**: property

A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fileAttributes: [FileAttributeKey : Any]? { get }
```

#### Discussion

See the description of the [`fileAttributes(atPath:traverseLink:)`](filemanager/fileattributes(atpath:traverselink:).md) method of [`FileManager`](filemanager.md) for details on obtaining the attributes from the dictionary.

## See Also

- [var directoryAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/directoryattributes.md)
  A dictionary with the attributes of the directory at which enumeration started.
- [var level: Int](filemanager/directoryenumerator/level.md)
  The number of levels deep the current object is in the directory hierarchy being enumerated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/fileattributes)*