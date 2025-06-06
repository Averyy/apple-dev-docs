# decodeObject(of:forKey:)

**Framework**: Foundation  
**Kind**: method

Decode an object as an expected type, failing if the archived type doesn’t match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func decodeObject<DecodedObjectType>(of cls: DecodedObjectType.Type, forKey key: String) -> DecodedObjectType? where DecodedObjectType : NSObject, DecodedObjectType : NSCoding
```

#### Return Value

The decoded object, or `nil` if decoding fails.

#### Discussion

If the coder responds [`true`](https://developer.apple.com/documentation/swift/true) to [`requiresSecureCoding`](nscoder/requiressecurecoding.md), then the coder calls [`failWithError(_:)`](nscoder/failwitherror(_:).md) in either of the following cases:

- The class indicated by `cls` doesn’t implement [`NSSecureCoding`](nssecurecoding.md).
- The unarchived class doesn’t match `cls`, nor do any of its superclasses.

If the coder doesn’t require secure coding, it ignores the `cls` parameter and does not check the decoded object.

## Parameters

- `cls`: The expected class of the object being decoded.
- `key`: The key indicating the member to decode.

## See Also

- [func decodeObject(of: [AnyClass]?, forKey: String) -> Any?](nscoder/decodeobject(of:forkey:)-roif.md)
  Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [func decodeTopLevelObject() throws -> Any?](nscoder/decodetoplevelobject.md)
  Decodes a previously-encoded object.
- [func decodeTopLevelObject(forKey: String) throws -> Any?](nscoder/decodetoplevelobject(forkey:)-7cram.md)
  Decodes the previously-encoded object associated by a key.
- [func decodeTopLevelObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?](nscoder/decodetoplevelobject(of:forkey:)-3w6pd.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [func decodeTopLevelObject(of: [AnyClass]?, forKey: String) throws -> Any?](nscoder/decodetoplevelobject(of:forkey:)-5lnnn.md)
  Decode an object as one of several expected types, failing if the archived type does not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodeobject(of:forkey:)-7tmft)*