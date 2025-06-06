# archivedData(withRootObject:)

**Framework**: Foundation  
**Kind**: method

Returns a data object that contains the encoded form of the object graph formed by the given root object.

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
class func archivedData(withRootObject rootObject: Any) -> Data
```

#### Return Value

An `NSData` object containing the encoded form of the object graph whose root object is `rootObject`. The format of the archive is [`PropertyListSerialization.PropertyListFormat.binary`](propertylistserialization/propertylistformat/binary.md).

## Parameters

- `rootObject`: The root of the object graph to archive.

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
- [class func archiveRootObject(Any, toFile: String) -> Bool](nskeyedarchiver/archiverootobject(_:tofile:).md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:))*