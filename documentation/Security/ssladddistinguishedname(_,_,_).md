# SSLAddDistinguishedName(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Adds a DER-encoded distinguished name to a list of acceptable names to be specified in requests for client certificates.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafeRawPointer?, _ derDNLen: Int) -> OSStatus
```

```c
OSStatus SSLAddDistinguishedName(SSLContextRef context, const void *derDN, size_t derDNLen);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `derDN`: A pointer to a buffer containing a DER-encoded distinguished name.
- `derDNLen`: A value of type `size_t` representing the size of the buffer pointed to by the parameter `derDN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ssladddistinguishedname(_:_:_:))*