# SSLAddDistinguishedName(_:_:_:)

**Framework**: Security  
**Kind**: func

Adds a DER-encoded distinguished name to a list of acceptable names to be specified in requests for client certificates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafeRawPointer?, _ derDNLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `derDN`: A pointer to a buffer containing a DER-encoded distinguished name.
- `derDNLen`: A value of type   representing the size of the buffer pointed to by the parameter  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ssladddistinguishedname(_:_:_:))*