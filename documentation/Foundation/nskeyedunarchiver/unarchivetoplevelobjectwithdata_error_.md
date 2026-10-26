# unarchiveTopLevelObjectWithData:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes a previously-archived object graph, returning the root object.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

## Declaration

```objc
+ (id) unarchiveTopLevelObjectWithData:(NSData *) data error:(NSError **) error;
```

#### Return Value

The unarchived object, or `nil` if an error occurred.

#### Discussion

This method produces an error if `data` does not contain valid keyed data.

## Parameters

- `data`: An object graph previously encoded by [`NSKeyedArchiver`](../nskeyedarchiver.md).
- `error`: On output, an error encountered during decoding, or `nil` if no error occurred.

## See Also

### Unarchiving Data
- [+ unarchivedObjectOfClass:fromData:error:](./unarchivedobjectofclass_fromdata_error_.md)
  Decodes a previously-archived object graph, that returns the root object as the specified type.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](./unarchivedobject%28ofclasses,from%29-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata:error:)*