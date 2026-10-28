# archiveRootObject(_:toFile:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Archives an object graph rooted at a given object to a file at a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use +archivedDataWithRootObject:requiringSecureCoding:error: and -writeToURL:options:error: instead

## Declaration

```swift
class func archiveRootObject(_ rootObject: Any, toFile path: String) -> Bool
```

```objc
+ (BOOL) archiveRootObject:(id) rootObject toFile:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) if the operation was successful, otherwise [`false`](../../Swift/false.md).

## Discussion

This method archives the graph formed by the root object to a data object, then atomically writes it to the given path. The format of the archive is [`PropertyListSerialization.PropertyListFormat.binary`](../propertylistserialization/propertylistformat/binary.md).

## Parameters

- `rootObject`: The root of the object graph to archive.
- `path`: The path of the file in which to write the archive.

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
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](./archiveddata%28withrootobject%29.md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiverootobject(_:tofile:))*