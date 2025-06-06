# SSLSetDiffieHellmanParams(_:_:_:)

**Framework**: Security  
**Kind**: func

Specifies Diffie-Hellman parameters for a given context.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SSLSetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeRawPointer?, _ dhParamsLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

You can use this function to specify a set of Diffie-Hellman parameters to be used by Secure Transport for a specific session. Use of this function is optional. If Diffie-Hellman ciphers are allowed, the server and client negotiate a Diffie-Hellman cipher, and this function has not been called, then secure transport calculates a set of process wide parameters. However, that process can take as long as 30 seconds. Diffie-Hellman ciphers are enabled by default. See [`SSLSetEnabledCiphers(_:_:_:)`](sslsetenabledciphers(_:_:_:).md).

In SSL/TLS, Diffie-Hellman parameters are always specified by the server. Therefore, this function can be called only by the server side of the connection.

You can use the [`SSLGetDiffieHellmanParams(_:_:_:)`](sslgetdiffiehellmanparams(_:_:_:).md) function to retrieve Diffie-Hellman parameters specified in an earlier call to [`SSLSetDiffieHellmanParams(_:_:_:)`](sslsetdiffiehellmanparams(_:_:_:).md).

## Parameters

- `context`: An SSL session context reference.
- `dhParams`: A pointer to a buffer containing the Diffie-Hellman parameters in Open SSL DER format.
- `dhParamsLen`: A value representing the size of the buffer pointed to by the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetdiffiehellmanparams(_:_:_:))*