# decodeTopLevelObject(of:forKey:)

**Framework**: Foundation  
**Kind**: method

Decode an object as one of several expected types, failing if the archived type does not match.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@nonobjc
func decodeTopLevelObject(of classes: [AnyClass]?, forKey key: String) throws -> Any?
```

#### Return Value

The decoded object, or `nil` if decoding fails.

#### Discussion

This method is equivalent to [`decodeObject(of:forKey:)`](nscoder/decodeobject(of:forkey:)-7tmft.md), but allows you to specify a set of classes that the decoded object can match. If [`requiresSecureCoding`](nscoder/requiressecurecoding.md) is `true`, the decoded object’s class must be a member of the classes parameter, or a sublcass of a member.

## Parameters

- `classes`: An array of expected classes that the object being decoded should match at least one of.
- `key`: The key indicating the member to decode.

## See Also

- [func decodeObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) -> DecodedObjectType?](nscoder/decodeobject(of:forkey:)-7tmft.md)
  Decode an object as an expected type, failing if the archived type doesn’t match.
- [func decodeObject(of: [AnyClass]?, forKey: String) -> Any?](nscoder/decodeobject(of:forkey:)-roif.md)
  Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [func decodeTopLevelObject() throws -> Any?](nscoder/decodetoplevelobject.md)
  Decodes a previously-encoded object.
- [func decodeTopLevelObject(forKey: String) throws -> Any?](nscoder/decodetoplevelobject(forkey:)-7cram.md)
  Decodes the previously-encoded object associated by a key.
- [func decodeTopLevelObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?](nscoder/decodetoplevelobject(of:forkey:)-3w6pd.md)
  Decode an object as one of several expected types, failing if the archived type does not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject(of:forkey:)-5lnnn)*