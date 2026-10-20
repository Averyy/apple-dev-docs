# createRootCertificate(_:issuerID:fabricID:validityPeriod:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- tvOS 16.6+
- visionOS 1.0+
- watchOS 9.6+

## Declaration

```swift
class func createRootCertificate(_ keypair: any MTRKeypair, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data
```

```objc
+ (MTRCertificateDERBytes) createRootCertificate:(id<MTRKeypair>) keypair issuerID:(NSNumber *) issuerID fabricID:(NSNumber *) fabricID validityPeriod:(NSDateInterval *) validityPeriod error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createrootcertificate(_:issuerid:fabricid:validityperiod:))*