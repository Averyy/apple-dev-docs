# encodedData

**Framework**: Foundation  
**Kind**: property

The encoded data for the archiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var encodedData: Data { get }
```

#### Discussion

If encoding has not yet finished, invoking this property calls [`finishEncoding()`](nskeyedarchiver/finishencoding().md) and populates this property with the encoded data. If you initialized the keyed archiver with [`init(forWritingWith:)`](nskeyedarchiver/init(forwritingwith:).md) and a specific mutable data instance, this property contains that instance.

## See Also

- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:).md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](nskeyedarchiver/finishencoding.md)
  Instructs the receiver to construct the final data stream.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](nskeyedarchiver/outputformat.md)
  The format in which the receiver encodes its data.
- [var requiresSecureCoding: Bool](nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](nskeyedarchiver/archiveddata(withrootobject:).md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nskeyedarchiver/archiverootobject(_:tofile:).md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodeddata)*