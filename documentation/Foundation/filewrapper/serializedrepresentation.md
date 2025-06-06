# serializedRepresentation

**Framework**: Foundation  
**Kind**: property

The contents of the file wrapper as an opaque data object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var serializedRepresentation: Data? { get }
```

#### Discussion

This property contains a data object in the format used by the [`fileContents`](https://developer.apple.com/documentation/AppKit/NSPasteboard/PasteboardType/fileContents) pasteboard type. This data object is also suitable for passing to [`init(serializedRepresentation:)`](filewrapper/init(serializedrepresentation:).md).

This property may be `nil` if the user modifies the contents of the file system node after you call [`read(from:options:)`](filewrapper/read(from:options:).md) or [`init(url:options:)`](filewrapper/init(url:options:).md), but before [`FileWrapper`](filewrapper.md) has read the contents of the file.  You can use the [`immediate`](filewrapper/readingoptions/immediate.md) reading option to reduce the likelihood of this problem.

## See Also

- [init?(serializedRepresentation: Data)](filewrapper/init(serializedrepresentation:).md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/serializedrepresentation)*