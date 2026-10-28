# archivedData(withRootObject:requiringSecureCoding:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func archivedData(withRootObject object: Any, requiringSecureCoding requiresSecureCoding: Bool) throws -> Data
```

```objc
+ (NSData *) archivedDataWithRootObject:(id) object requiringSecureCoding:(BOOL) requiresSecureCoding error:(NSError **) error;
```

## Discussion

To prevent the possibility of encoding an object that [`NSKeyedUnarchiver`](../nskeyedunarchiver.md) can’t decode, set `requiresSecureCoding` to true whenever possible. This ensures that all encoded objects conform to [`NSSecureCoding`](../nssecurecoding.md).

> **Note**:  Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## Parameters

- `object`: The root of the object graph to archive.
- `requiresSecureCoding`: A Boolean value indicating whether all encoded objects must conform to [`NSSecureCoding`](../nssecurecoding.md).

## See Also

### Archiving Data
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
- [class func archiveRootObject(Any, toFile: String) -> Bool](./archiverootobject%28_,tofile%29.md)
  Archives an object graph rooted at a given object to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/archiveddata(withrootobject:requiringsecurecoding:))*