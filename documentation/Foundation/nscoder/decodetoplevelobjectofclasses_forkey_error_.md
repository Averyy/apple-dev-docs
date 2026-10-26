# decodeTopLevelObjectOfClasses:forKey:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decode an object as one of several expected types, failing if the archived type does not match.

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
- (id) decodeTopLevelObjectOfClasses:(NSSet<Class> *) classes forKey:(NSString *) key error:(NSError **) error;
```

#### Return Value

The decoded object, or `nil` if decoding fails.

#### Discussion

This method is equivalent to [`decodeObject(of:forKey:)`](./decodeobject%28of,forkey%29-roif.md), but allows you to specify a set of classes that the decoded object can match. If [`requiresSecureCoding`](./requiressecurecoding.md) is [`true`](../../Swift/true.md), the decoded object’s class must be a member of the classes parameter, or a sublcass of a member.

## Parameters

- `classes`: A set of expected classes that the object being decoded should match at least one of.
- `key`: The archive key indicating the member to decode.
- `error`: On return, an [`NSError`](../nserror.md) indicating why decoding failed, or `nil` if no error occurred.

## See Also

### Decoding Top-Level Objects
- [- decodeTopLevelObjectOfClass:forKey:error:](./decodetoplevelobjectofclass_forkey_error_.md)
  Decode an object as an expected type, failing if the archived type does not match.
- [- decodeTopLevelObjectAndReturnError:](./decodetoplevelobjectandreturnerror_.md)
  Decodes a previously-encoded object, populating an error if decoding fails.
- [- decodeTopLevelObjectForKey:error:](./decodetoplevelobjectforkey_error_.md)
  Decodes the previously-encoded object associated by a key, populating an error if decoding fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectofclasses:forkey:error:)*