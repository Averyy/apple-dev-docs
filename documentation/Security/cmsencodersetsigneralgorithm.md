# CMSEncoderSetSignerAlgorithm(_:_:)

**Framework**: Security  
**Kind**: func

Sets the digest algorithm to use for the signer.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func CMSEncoderSetSignerAlgorithm(_ cmsEncoder: CMSEncoder, _ digestAlgorithm: CFString) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `digestAlgorithm`: A string representing the digest algorithm to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersetsigneralgorithm(_:_:))*