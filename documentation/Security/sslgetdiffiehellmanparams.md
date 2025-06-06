# SSLGetDiffieHellmanParams(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the Diffie-Hellman parameters for a given context.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SSLGetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeMutablePointer<UnsafeRawPointer?>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function returns the parameter block specified in an earlier call to the [`SSLSetDiffieHellmanParams(_:_:_:)`](sslsetdiffiehellmanparams(_:_:_:).md) function. If that function was never called, the `dhParams` parameter returns `NULL` and the `dhParamsLen` parameter returns `0`.

## Parameters

- `context`: An SSL session context reference.
- `dhParams`: On return, points to a buffer containing the Diffie-Hellman parameter block in Open SSL DER format.The returned data is not copied and belongs to the SSL session context reference; therefore, you cannot modify the data and it is released automatically when you dispose of the context.
- `dhParamsLen`: On return, points to the length of the buffer pointed to by the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetdiffiehellmanparams(_:_:_:))*