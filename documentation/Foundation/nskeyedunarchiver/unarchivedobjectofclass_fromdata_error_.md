# unarchivedObjectOfClass:fromData:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes a previously-archived object graph, that returns the root object as the specified type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
+ (id) unarchivedObjectOfClass:(Class) cls fromData:(NSData *) data error:(NSError **) error;
```

#### Return Value

The decoded root of the object graph, or `nil` if an error occurred.

#### Discussion

This method produces an error if `data` does not contain valid keyed data.

> ❗ **Important**:  Make sure you have adopted [`NSSecureCoding`](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [`decodingFailurePolicy`](./decodingfailurepolicy.md) sets the error rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## Parameters

- `cls`: The expected class of the root object.
- `data`: An object graph previously encoded by [`NSKeyedArchiver`](../nskeyedarchiver.md).
- `error`: If the return value is `nil`, an [`NSError`](../nserror.md) indicating why the unarchive operation failed.

## See Also

### Unarchiving Data
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](./unarchivedobject%28ofclasses,from%29-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [+ unarchiveTopLevelObjectWithData:error:](./unarchivetoplevelobjectwithdata_error_.md)
  Decodes a previously-archived object graph, returning the root object.
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedobjectofclass:fromdata:error:)*