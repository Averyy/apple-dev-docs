# unarchivedObject(ofClass:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes a previously-archived object graph, and returns the root object as the specified type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@nonobjc
static func unarchivedObject<DecodedObjectType>(ofClass cls: DecodedObjectType.Type, from data: Data) throws -> DecodedObjectType? where DecodedObjectType : NSObject, DecodedObjectType : NSCoding
```

## Return Value

The decoded root of the object graph, or `nil` if an error occurred.

## Discussion

This method produces an error if `data` does not contain valid keyed data.

> ❗ **Important**:  Make sure you have adopted [`NSSecureCoding`](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [`decodingFailurePolicy`](./decodingfailurepolicy.md) sets the error rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## Parameters

- `cls`: The expected class of the root object.
- `data`: An object graph previously encoded by [`NSKeyedArchiver`](../nskeyedarchiver.md).

## See Also

### Unarchiving Data
- [class func unarchiveTopLevelObjectWithData(Data) throws -> Any?](./unarchivetoplevelobjectwithdata%28_%29.md)
  Decodes a previously-archived object graph, and returns the root object.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](./unarchivedobject%28ofclasses,from%29-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](./unarchivedobject%28ofclasses,from%29-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](../nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](./unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedobject(ofclass:from:))*