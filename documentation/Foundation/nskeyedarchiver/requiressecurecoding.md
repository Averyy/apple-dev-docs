# requiresSecureCoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readwrite) BOOL requiresSecureCoding;
```

#### Discussion

If you set the archiver to require secure coding, it throws an exception if you attempt to archive a class which doesn’t conform to [`NSSecureCoding`](../nssecurecoding.md).

Note that the getter is on the superclass, [`NSCoder`](../nscoder.md). See [`NSCoder`](../nscoder.md) for more information about secure coding.

> **Note**:  Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the receiver requires [`NSSecureCoding`](../nssecurecoding.md); [`false`](../../Swift/false.md) if not.

## See Also

### Archiving Data
- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](./archiveddata%28withrootobject,requiringsecurecoding%29.md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](./finishencoding%28%29.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](./encodeddata.md)
  The encoded data for the archiver.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](./outputformat.md)
  The format in which the receiver encodes its data.
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/requiressecurecoding)*