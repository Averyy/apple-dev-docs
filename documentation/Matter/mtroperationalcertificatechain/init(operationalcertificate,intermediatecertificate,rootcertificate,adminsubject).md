# init(operationalCertificate:intermediateCertificate:rootCertificate:adminSubject:)

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
init(operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data, adminSubject: NSNumber?)
```

```objc
- (instancetype) initWithOperationalCertificate:(MTRCertificateDERBytes) operationalCertificate intermediateCertificate:(MTRCertificateDERBytes) intermediateCertificate rootCertificate:(MTRCertificateDERBytes) rootCertificate adminSubject:(NSNumber *) adminSubject;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtroperationalcertificatechain/init(operationalcertificate:intermediatecertificate:rootcertificate:adminsubject:))*