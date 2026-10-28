# decodeXPCObject(ofType:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes an object and validates that its type matches the type a service provides over XPC.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func decodeXPCObject(ofType type: xpc_type_t, forKey key: String) -> xpc_object_t?
```

```objc
- (xpc_object_t) decodeXPCObjectOfType:(xpc_type_t) type forKey:(NSString *) key;
```

## Return Value

An object that XPC can encode.

## Discussion

The [`decodeXPCObject(ofType:forKey:)`](./decodexpcobject%28oftype,forkey%29.md) method validates that the type of the decoded object matches the type of the encoded object. If they don’t match, the [`NSXPCCoder`](../nsxpccoder.md) throws an exception in support of [`NSSecureCoding`](../nssecurecoding.md).

Be sure to check the result against [`null`](../nsnull/null.md) if you call an [XPC](../../XPC/XPC.md) function because calling an [XPC](../../XPC/XPC.md) function on a [`null`](../nsnull/null.md) object results in a crash.

## Parameters

- `type`: An opaque pointer to an encoded XPC object.
- `key`: A string that your app uses to reference the decoded object.

## See Also

### Encoding and Decoding
- [func encodeXPCObject(xpc_object_t, forKey: String)](./encodexpcobject%28_,forkey%29.md)
  Encodes an object to send over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder/decodexpcobject(oftype:forkey:))*