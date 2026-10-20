# onNOCChainGenerationNeeded(_:attestationInfo:onNOCChainGenerationComplete:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTROperationalCertificateIssuer

## Declaration

```swift
func onNOCChainGenerationNeeded(_ csrInfo: CSRInfo, attestationInfo: AttestationInfo, onNOCChainGenerationComplete: @escaping MTRNOCChainGenerationCompleteHandler)
```

```objc
- (void) onNOCChainGenerationNeeded:(CSRInfo *) csrInfo attestationInfo:(AttestationInfo *) attestationInfo onNOCChainGenerationComplete:(MTRNOCChainGenerationCompleteHandler) onNOCChainGenerationComplete;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrnocchainissuer/onnocchaingenerationneeded(_:attestationinfo:onnocchaingenerationcomplete:))*