# decodeXPCObject(ofType:forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes an object and validates that its type matches the type a service provides over XPC.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
func decodeXPCObject(ofType type: xpc_type_t, forKey key: String) -> xpc_object_t?
```

#### Return Value

An object that XPC can encode.

#### Discussion

The [`decodeXPCObject(ofType:forKey:)`](nsxpccoder/decodexpcobject(oftype:forkey:).md) method validates that the type of the decoded object matches the type of the encoded object. If they don’t match, the [`NSXPCCoder`](nsxpccoder.md) throws an exception in support of [`NSSecureCoding`](nssecurecoding.md).

Be sure to check the result against [`null`](nsnull/null.md) if you call an [`XPC`](https://developer.apple.com/documentation/XPC) function because calling an [`XPC`](https://developer.apple.com/documentation/XPC) function on a [`null`](nsnull/null.md) object results in a crash.

## Parameters

- `type`: An opaque pointer to an encoded XPC object.
- `key`: A string that your app uses to reference the decoded object.

## See Also

- [func encodeXPCObject(xpc_object_t, forKey: String)](nsxpccoder/encodexpcobject(_:forkey:).md)
  Encodes an object to send over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/decodexpcobject(oftype:forkey:))*