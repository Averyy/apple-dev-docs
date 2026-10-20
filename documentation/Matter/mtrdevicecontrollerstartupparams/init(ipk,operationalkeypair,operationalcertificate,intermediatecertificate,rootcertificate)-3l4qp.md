# init(ipk:operationalKeypair:operationalCertificate:intermediateCertificate:rootCertificate:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
init(ipk: Data, operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data)
```

```objc
- (instancetype) initWithIPK:(NSData *) ipk operationalKeypair:(id<MTRKeypair>) operationalKeypair operationalCertificate:(MTRCertificateDERBytes) operationalCertificate intermediateCertificate:(MTRCertificateDERBytes) intermediateCertificate rootCertificate:(MTRCertificateDERBytes) rootCertificate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstartupparams/init(ipk:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:)-3l4qp)*