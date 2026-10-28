# decodeTopLevelObjectForKey:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes the previously-encoded object associated by a key, populating an error if decoding fails.

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
- (id) decodeTopLevelObjectForKey:(NSString *) key error:(NSError **) error;
```

## Return Value

The decoded object, or `nil` if decoding fails.

## Parameters

- `key`: The key that identifies the object to decode.
- `error`: An [`NSError`](../nserror.md) reference. On return, if this value is not `nil`, it represents an error encountered while decoding.

## See Also

### Decoding Top-Level Objects
- [- decodeTopLevelObjectOfClass:forKey:error:](./decodetoplevelobjectofclass_forkey_error_.md)
  Decode an object as an expected type, failing if the archived type does not match.
- [- decodeTopLevelObjectOfClasses:forKey:error:](./decodetoplevelobjectofclasses_forkey_error_.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [- decodeTopLevelObjectAndReturnError:](./decodetoplevelobjectandreturnerror_.md)
  Decodes a previously-encoded object, populating an error if decoding fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetoplevelobjectforkey:error:)*