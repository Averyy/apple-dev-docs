# outputFormat

**Framework**: Foundation  
**Kind**: property

The format in which the receiver encodes its data.

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
var outputFormat: PropertyListSerialization.PropertyListFormat { get set }
```

#### Discussion

The available formats are [`PropertyListSerialization.PropertyListFormat.xml`](propertylistserialization/propertylistformat/xml.md) and [`PropertyListSerialization.PropertyListFormat.binary`](propertylistserialization/propertylistformat/binary.md).

## See Also

- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:).md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](nskeyedarchiver/finishencoding.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](nskeyedarchiver/encodeddata.md)
  The encoded data for the archiver.
- [var requiresSecureCoding: Bool](nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](nskeyedarchiver/archiveddata(withrootobject:).md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nskeyedarchiver/archiverootobject(_:tofile:).md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/outputformat)*