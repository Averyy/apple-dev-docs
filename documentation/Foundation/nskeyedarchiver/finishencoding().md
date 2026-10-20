# finishEncoding()

**Framework**: Foundation  
**Kind**: method

Instructs the receiver to construct the final data stream.

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
func finishEncoding()
```

#### Discussion

No more values can be encoded after this method is called. You must call this method when finished.

## See Also

- [init(forWritingWith: NSMutableData)](nskeyedarchiver/init(forwritingwith:).md)
  Initializes an archiver to encode data into a given a mutable-data object.
- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:).md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [var encodedData: Data](nskeyedarchiver/encodeddata.md)
  The encoded data for the archiver.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](nskeyedarchiver/outputformat.md)
  The format in which the receiver encodes its data.
- [var requiresSecureCoding: Bool](nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](nskeyedarchiver/archiveddata(withrootobject:).md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nskeyedarchiver/archiverootobject(_:tofile:).md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/finishencoding())*