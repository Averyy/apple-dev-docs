# FileManager.URLRelationship

**Framework**: Foundation  
**Kind**: enum

Constants indicating the relationship between a directory and an item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum URLRelationship
```

## Topics

### URL Relationships
- [FileManager.URLRelationship.contains](filemanager/urlrelationship/contains.md)
  The directory contains the specified item.
- [FileManager.URLRelationship.same](filemanager/urlrelationship/same.md)
  The directory and the item are the same. This relationship occurs when the value of the [`fileResourceIdentifierKey`](urlresourcekey/fileresourceidentifierkey.md) is the same for the directory and item.
- [FileManager.URLRelationship.other](filemanager/urlrelationship/other.md)
  The directory does not contain the item and is not the same as the item.
### Initializers
- [init?(rawValue: Int)](filemanager/urlrelationship/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, ofDirectoryAt: URL, toItemAt: URL) throws](filemanager/getrelationship(_:ofdirectoryat:toitemat:).md)
  Determines the type of relationship that exists between a directory and an item.
- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, of: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, toItemAt: URL) throws](filemanager/getrelationship(_:of:in:toitemat:).md)
  Determines the type of relationship that exists between a system directory and the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/urlrelationship)*