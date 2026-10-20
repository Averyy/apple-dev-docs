# encodeXPCObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes an object to send over an XPC connection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func encodeXPCObject(_ xpcObject: xpc_object_t, forKey key: String)
```

```objc
- (void) encodeXPCObject:(xpc_object_t) xpcObject forKey:(NSString *) key;
```

## Parameters

- `xpcObject`: An object that XPC can encode.
- `key`: A string that your app uses to reference the encoded object.

## See Also

### Encoding and Decoding
- [func decodeXPCObject(ofType: xpc_type_t, forKey: String) -> xpc_object_t?](./decodexpcobject%28oftype,forkey%29.md)
  Decodes an object and validates that its type matches the type a service provides over XPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/encodexpcobject(_:forkey:))*