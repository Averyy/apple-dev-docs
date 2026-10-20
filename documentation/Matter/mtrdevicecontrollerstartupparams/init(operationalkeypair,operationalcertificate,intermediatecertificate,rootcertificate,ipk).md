# init(operationalKeypair:operationalCertificate:intermediateCertificate:rootCertificate:ipk:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use initWithIPK:operationalKeypair:operationalCertificate:intermediateCertificate:rootCertificate:

## Declaration

```swift
init(operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data, ipk: Data)
```

```objc
- (instancetype) initWithOperationalKeypair:(id<MTRKeypair>) operationalKeypair operationalCertificate:(MTRCertificateDERBytes) operationalCertificate intermediateCertificate:(MTRCertificateDERBytes) intermediateCertificate rootCertificate:(MTRCertificateDERBytes) rootCertificate ipk:(NSData *) ipk;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstartupparams/init(operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:ipk:))*