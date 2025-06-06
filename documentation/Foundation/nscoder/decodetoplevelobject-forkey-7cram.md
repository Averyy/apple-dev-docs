# decodeTopLevelObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes the previously-encoded object associated by a key.

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
func decodeTopLevelObject(forKey key: String) throws -> Any?
```

#### Return Value

The decoded object, or `nil` if decoding fails.

## Parameters

- `key`: The key that identifies the object to decode.

## See Also

- [func decodeObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) -> DecodedObjectType?](nscoder/decodeobject(of:forkey:)-7tmft.md)
  Decode an object as an expected type, failing if the archived type doesn’t match.
- [func decodeObject(of: [AnyClass]?, forKey: String) -> Any?](nscoder/decodeobject(of:forkey:)-roif.md)
  Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [func decodeTopLevelObject() throws -> Any?](nscoder/decodetoplevelobject.md)
  Decodes a previously-encoded object.
- [func decodeTopLevelObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?](nscoder/decodetoplevelobject(of:forkey:)-3w6pd.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [func decodeTopLevelObject(of: [AnyClass]?, forKey: String) throws -> Any?](nscoder/decodetoplevelobject(of:forkey:)-5lnnn.md)
  Decode an object as one of several expected types, failing if the archived type does not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject(forkey:)-7cram)*