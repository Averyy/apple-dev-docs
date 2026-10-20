# outputFormat

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSPropertyListFormat outputFormat;
```

#### Discussion

The available formats are [`PropertyListSerialization.PropertyListFormat.xml`](../propertylistserialization/propertylistformat/xml.md) and [`PropertyListSerialization.PropertyListFormat.binary`](../propertylistserialization/propertylistformat/binary.md).

## See Also

### Archiving Data
- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](./archiveddata%28withrootobject,requiringsecurecoding%29.md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](./finishencoding%28%29.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](./encodeddata.md)
  The encoded data for the archiver.
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/outputformat)*