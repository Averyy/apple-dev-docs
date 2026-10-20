# FileManager.URLRelationship

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSURLRelationship : NSInteger;
```

## Topics

### URL Relationships
- [FileManager.URLRelationship.contains](./urlrelationship/contains.md)
  The directory contains the specified item.
- [FileManager.URLRelationship.same](./urlrelationship/same.md)
  The directory and the item are the same. This relationship occurs when the value of the [`fileResourceIdentifierKey`](../urlresourcekey/fileresourceidentifierkey.md) is the same for the directory and item.
- [FileManager.URLRelationship.other](./urlrelationship/other.md)
  The directory does not contain the item and is not the same as the item.
### Initializers
- [init?(rawValue: Int)](./urlrelationship/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the relationship between items
- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, ofDirectoryAt: URL, toItemAt: URL) throws](./getrelationship%28_,ofdirectoryat,toitemat%29.md)
  Determines the type of relationship that exists between a directory and an item.
- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, of: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, toItemAt: URL) throws](./getrelationship%28_,of,in,toitemat%29.md)
  Determines the type of relationship that exists between a system directory and the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/urlrelationship)*