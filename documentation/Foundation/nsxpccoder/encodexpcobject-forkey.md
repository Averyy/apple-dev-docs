# encodeXPCObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes an object to send over an XPC connection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func encodeXPCObject(_ xpcObject: xpc_object_t, forKey key: String)
```

## Parameters

- `xpcObject`: An object that XPC can encode.
- `key`: A string that your app uses to reference the encoded object.

## See Also

- [func decodeXPCObject(ofType: xpc_type_t, forKey: String) -> xpc_object_t?](nsxpccoder/decodexpcobject(oftype:forkey:).md)
  Decodes an object and validates that its type matches the type a service provides over XPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/encodexpcobject(_:forkey:))*