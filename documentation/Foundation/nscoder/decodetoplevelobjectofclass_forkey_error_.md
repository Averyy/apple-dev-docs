# decodeTopLevelObjectOfClass:forKey:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decode an object as an expected type, failing if the archived type does not match.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (id) decodeTopLevelObjectOfClass:(Class) aClass forKey:(NSString *) key error:(NSError **) error;
```

#### Return Value

The decoded object, or `nil` if decoding fails.

#### Discussion

If the coder responds [`true`](../../Swift/true.md) to [`requiresSecureCoding`](./requiressecurecoding.md), then the coder calls [`failWithError(_:)`](./failwitherror%28_%29.md) in either the following cases:

- The class indicated by `cls` does not implement [`NSSecureCoding`](../nssecurecoding.md).
- The unarchived class does not match `cls`, nor do any of its superclasses.

If the coder does not require secure coding, it ignores the `cls` parameter and does not check the decoded object.

## Parameters

- `aClass`: The expected class of the object being decoded.
- `key`: The archive key indicating the member to decode.
- `error`: On return, an [`NSError`](../nserror.md) indicating why decoding failed, or `nil` if no error occurred.

## See Also

### Decoding Top-Level Objects
- [- decodeTopLevelObjectOfClasses:forKey:error:](./decodetoplevelobjectofclasses_forkey_error_.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [- decodeTopLevelObjectAndReturnError:](./decodetoplevelobjectandreturnerror_.md)
  Decodes a previously-encoded object, populating an error if decoding fails.
- [- decodeTopLevelObjectForKey:error:](./decodetoplevelobjectforkey_error_.md)
  Decodes the previously-encoded object associated by a key, populating an error if decoding fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectofclass:forkey:error:)*