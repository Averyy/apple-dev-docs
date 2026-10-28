# unarchivedObject(ofClasses:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes a previously-archived object graph, returning the root object as one of the specified classes.

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
class func unarchivedObject(ofClasses classes: Set<AnyHashable>, from data: Data) throws -> Any
```

```objc
+ (id) unarchivedObjectOfClasses:(NSSet<Class> *) classes fromData:(NSData *) data error:(NSError **) error;
```

## Return Value

The decoded root of the object graph, as an instance of one of the specified classes, or `nil` if an error occurred.

## Discussion

This method produces an error if data does not contain valid keyed data.

> ❗ **Important**:  Make sure you have adopted [`NSSecureCoding`](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [`decodingFailurePolicy`](./decodingfailurepolicy.md) sets the error rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## Parameters

- `classes`: A set of classes, at least one of which the root object should conform to.
- `data`: An object graph previously encoded by [`NSKeyedArchiver`](../nskeyedarchiver.md).

## See Also

### Unarchiving Data
- [class func unarchiveTopLevelObjectWithData(Data) throws -> Any?](./unarchivetoplevelobjectwithdata%28_%29.md)
  Decodes a previously-archived object graph, and returns the root object.
- [static func unarchivedObject<DecodedObjectType>(ofClass: DecodedObjectType.Type, from: Data) throws -> DecodedObjectType?](./unarchivedobject%28ofclass,from%29.md)
  Decodes a previously-archived object graph, and returns the root object as the specified type.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](./unarchivedobject%28ofclasses,from%29-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.
- [+ unarchivedObjectOfClass:fromData:error:](./unarchivedobjectofclass_fromdata_error_.md)
  Decodes a previously-archived object graph, that returns the root object as the specified type.
- [+ unarchiveTopLevelObjectWithData:error:](./unarchivetoplevelobjectwithdata_error_.md)
  Decodes a previously-archived object graph, returning the root object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedobject(ofclasses:from:)-b9t5)*