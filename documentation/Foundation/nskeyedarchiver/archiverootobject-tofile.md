# archiveRootObject(_:toFile:)

**Framework**: Foundation  
**Kind**: method

Archives an object graph rooted at a given object to a file at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func archiveRootObject(_ rootObject: Any, toFile path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation was successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method archives the graph formed by the root object to a data object, then atomically writes it to the given path. The format of the archive is [`PropertyListSerialization.PropertyListFormat.binary`](propertylistserialization/propertylistformat/binary.md).

## Parameters

- `rootObject`: The root of the object graph to archive.
- `path`: The path of the file in which to write the archive.

## See Also

- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:).md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](nskeyedarchiver/finishencoding.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](nskeyedarchiver/encodeddata.md)
  The encoded data for the archiver.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](nskeyedarchiver/outputformat.md)
  The format in which the receiver encodes its data.
- [var requiresSecureCoding: Bool](nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](nskeyedarchiver/archiveddata(withrootobject:).md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiverootobject(_:tofile:))*