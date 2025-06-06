# unarchiveTopLevelObjectWithData(_:)

**Framework**: Foundation  
**Kind**: method

Decodes a previously-archived object graph, and returns the root object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 4.0+

## Declaration

```swift
@nonobjc
class func unarchiveTopLevelObjectWithData(_ data: Data) throws -> Any?
```

#### Return Value

The unarchived object, or `nil` if an error occurred.

#### Discussion

This method throws an error if `data` does not contain valid keyed data.

## Parameters

- `data`: An object graph previously encoded by  .

## See Also

- [static func unarchivedObject<DecodedObjectType>(ofClass: DecodedObjectType.Type, from: Data) throws -> DecodedObjectType?](nskeyedunarchiver/unarchivedobject(ofclass:from:).md)
  Decodes a previously-archived object graph, and returns the root object as the specified type.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](nskeyedunarchiver/unarchivedobject(ofclasses:from:)-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](nskeyedunarchiver/unarchivedobject(ofclasses:from:)-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](nskeyedunarchiver/requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](nskeyedunarchiver/unarchiveobject(with:).md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](nskeyedunarchiver/unarchiveobject(withfile:).md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivetoplevelobjectwithdata(_:)-40hyk)*