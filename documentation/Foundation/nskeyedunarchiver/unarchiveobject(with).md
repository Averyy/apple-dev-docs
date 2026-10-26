# unarchiveObject(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use +unarchivedObjectOfClass:fromData:error: instead

## Declaration

```swift
class func unarchiveObject(with data: Data) -> Any?
```

```objc
+ (id) unarchiveObjectWithData:(NSData *) data;
```

#### Return Value

The object graph previously encoded by `NSKeyedArchiver` and stored in `data`.

#### Discussion

This method raises an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) if `data` is not a valid archive.

## Parameters

- `data`: An object graph previously encoded by `NSKeyedArchiver`.

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
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.
- [+ unarchivedObjectOfClass:fromData:error:](./unarchivedobjectofclass_fromdata_error_.md)
  Decodes a previously-archived object graph, that returns the root object as the specified type.
- [+ unarchiveTopLevelObjectWithData:error:](./unarchivetoplevelobjectwithdata_error_.md)
  Decodes a previously-archived object graph, returning the root object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveobject(with:))*