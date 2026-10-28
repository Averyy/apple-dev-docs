# CMSEncoderSetSignerAlgorithm(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the digest algorithm to use for the signer.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func CMSEncoderSetSignerAlgorithm(_ cmsEncoder: CMSEncoder, _ digestAlgorithm: CFString) -> OSStatus
```

```c
OSStatus CMSEncoderSetSignerAlgorithm(CMSEncoderRef cmsEncoder, CFStringRef digestAlgorithm);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the [`CMSEncoderCreate(_:)`](./cmsencodercreate%28_%29.md) function.
- `digestAlgorithm`: A string representing the digest algorithm to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersetsigneralgorithm(_:_:))*