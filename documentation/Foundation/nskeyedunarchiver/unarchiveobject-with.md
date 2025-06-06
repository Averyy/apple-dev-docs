# unarchiveObject(with:)

**Framework**: Foundation  
**Kind**: method

Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func unarchiveObject(with data: Data) -> Any?
```

#### Return Value

The object graph previously encoded by `NSKeyedArchiver` and stored in `data`.

#### Discussion

This method raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if `data` is not a valid archive.

## Parameters

- `data`: An object graph previously encoded by  .

## See Also

- [class func unarchiveTopLevelObjectWithData(Data) throws -> Any?](nskeyedunarchiver/unarchivetoplevelobjectwithdata(_:)-40hyk.md)
  Decodes a previously-archived object graph, and returns the root object.
- [static func unarchivedObject<DecodedObjectType>(ofClass: DecodedObjectType.Type, from: Data) throws -> DecodedObjectType?](nskeyedunarchiver/unarchivedobject(ofclass:from:).md)
  Decodes a previously-archived object graph, and returns the root object as the specified type.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](nskeyedunarchiver/unarchivedobject(ofclasses:from:)-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](nskeyedunarchiver/unarchivedobject(ofclasses:from:)-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](nskeyedunarchiver/requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](nssecurecoding.md).
- [class func unarchiveObject(withFile: String) -> Any?](nskeyedunarchiver/unarchiveobject(withfile:).md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveobject(with:))*