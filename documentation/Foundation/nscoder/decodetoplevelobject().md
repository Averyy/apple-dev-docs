# decodeTopLevelObject()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a previously-encoded object.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2
- iPadOS 9.0+ - Deprecated in 27.2
- Mac Catalyst 9.0+ - Deprecated in 27.2
- macOS 10.11+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use decodeTopLevelObject(of:forKey:) instead

## Declaration

```swift
@nonobjc
func decodeTopLevelObject() throws -> Any?
```

#### Return Value

The decoded object, or `nil` if decoding fails.

## See Also

### Decoding Top-Level Objects
- [func decodeObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) -> DecodedObjectType?](./decodeobject%28of,forkey%29-7tmft.md)
  Decode an object as an expected type, failing if the archived type doesn’t match.
- [func decodeObject(of: [AnyClass]?, forKey: String) -> Any?](./decodeobject%28of,forkey%29-roif.md)
  Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [func decodeTopLevelObject(forKey: String) throws -> Any?](./decodetoplevelobject%28forkey%29.md)
  Decodes the previously-encoded object associated by a key.
- [func decodeTopLevelObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?](./decodetoplevelobject%28of,forkey%29-3w6pd.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [func decodeTopLevelObject(of: [AnyClass]?, forKey: String) throws -> Any?](./decodetoplevelobject%28of,forkey%29-5lnnn.md)
  Decode an object as one of several expected types, failing if the archived type does not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobject())*