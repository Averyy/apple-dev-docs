# directoryAttributes

**Framework**: Foundation  
**Kind**: property

A dictionary with the attributes of the directory at which enumeration started.

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
var directoryAttributes: [FileAttributeKey : Any]? { get }
```

#### Discussion

See the description of the [`fileAttributes(atPath:traverseLink:)`](filemanager/fileattributes(atpath:traverselink:).md) method of [`FileManager`](filemanager.md) for details on obtaining the attributes from the dictionary.

## See Also

- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [var fileAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/fileattributes.md)
  A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).
- [var level: Int](filemanager/directoryenumerator/level.md)
  The number of levels deep the current object is in the directory hierarchy being enumerated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/directoryattributes)*