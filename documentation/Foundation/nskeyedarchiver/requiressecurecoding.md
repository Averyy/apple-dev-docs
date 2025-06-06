# requiresSecureCoding

**Framework**: Foundation  
**Kind**: property

Indicates whether the archiver requires all archived classes to resist object substitution attacks.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var requiresSecureCoding: Bool { get set }
```

#### Discussion

If you set the archiver to require secure coding, it throws an exception if you attempt to archive a class which doesn’t conform to [`NSSecureCoding`](nssecurecoding.md).

Note that the getter is on the superclass, [`NSCoder`](nscoder.md). See [`NSCoder`](nscoder.md) for more information about secure coding.

> **Note**:  Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

 Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## Parameters

- `flag`:   if the receiver requires  ;   if not.

## See Also

- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:).md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](nskeyedarchiver/finishencoding.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](nskeyedarchiver/encodeddata.md)
  The encoded data for the archiver.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](nskeyedarchiver/outputformat.md)
  The format in which the receiver encodes its data.
- [class func archivedData(withRootObject: Any) -> Data](nskeyedarchiver/archiveddata(withrootobject:).md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nskeyedarchiver/archiverootobject(_:tofile:).md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/requiressecurecoding)*