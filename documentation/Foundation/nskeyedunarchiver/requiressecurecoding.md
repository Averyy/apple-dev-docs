# requiresSecureCoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).

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

## Discussion

If you set the receiver to require secure coding, it will throw an exception if you attempt to unarchive a class which does not conform to [`NSSecureCoding`](../nssecurecoding.md).

The secure coding requirement for [`NSKeyedUnarchiver`](../nskeyedunarchiver.md) is designed to be set once at the top level and remain on. Once enabled, attempting to call `setRequiresSecureCoding:` with a value of [`false`](../../Swift/false.md) will throw an exception. This is to prevent classes from selectively turning secure coding off.

Note that the getter is on the superclass, [`NSCoder`](../nscoder.md). See [`NSCoder`](../nscoder.md) for more information about secure coding.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the receiver requires [`NSSecureCoding`](../nssecurecoding.md); [`false`](../../Swift/false.md) if not.

## See Also

### Unarchiving Data
- [class func unarchiveTopLevelObjectWithData(Data) throws -> Any?](./unarchivetoplevelobjectwithdata%28_%29.md)
  Decodes a previously-archived object graph, and returns the root object.
- [static func unarchivedObject<DecodedObjectType>(ofClass: DecodedObjectType.Type, from: Data) throws -> DecodedObjectType?](./unarchivedobject%28ofclass,from%29.md)
  Decodes a previously-archived object graph, and returns the root object as the specified type.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](./unarchivedobject%28ofclasses,from%29-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](./unarchivedobject%28ofclasses,from%29-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.
- [+ unarchivedObjectOfClass:fromData:error:](./unarchivedobjectofclass_fromdata_error_.md)
  Decodes a previously-archived object graph, that returns the root object as the specified type.
- [+ unarchiveTopLevelObjectWithData:error:](./unarchivetoplevelobjectwithdata_error_.md)
  Decodes a previously-archived object graph, returning the root object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/requiressecurecoding)*