# level

**Framework**: Foundation  
**Kind**: property

The number of levels deep the current object is in the directory hierarchy being enumerated.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var level: Int { get }
```

#### Discussion

The number of levels, with the directory passed to [`enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:`](nsfilemanager/enumeratoraturl:includingpropertiesforkeys:options:errorhandler:.md) (`NSFileManager`) considered to be level `0`.

## See Also

- [var directoryAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/directoryattributes.md)
  A dictionary with the attributes of the directory at which enumeration started.
- [var fileAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/fileattributes.md)
  A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/level)*