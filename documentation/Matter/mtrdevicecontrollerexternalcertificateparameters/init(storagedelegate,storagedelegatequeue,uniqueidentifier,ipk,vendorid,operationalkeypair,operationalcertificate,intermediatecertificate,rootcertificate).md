# init(storageDelegate:storageDelegateQueue:uniqueIdentifier:ipk:vendorID:operationalKeypair:operationalCertificate:intermediateCertificate:rootCertificate:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
init(storageDelegate: any MTRDeviceControllerStorageDelegate, storageDelegateQueue: dispatch_queue_t, uniqueIdentifier: UUID, ipk: Data, vendorID: NSNumber, operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data)
```

```objc
- (instancetype) initWithStorageDelegate:(id<MTRDeviceControllerStorageDelegate>) storageDelegate storageDelegateQueue:(dispatch_queue_t) storageDelegateQueue uniqueIdentifier:(NSUUID *) uniqueIdentifier ipk:(NSData *) ipk vendorID:(NSNumber *) vendorID operationalKeypair:(id<MTRKeypair>) operationalKeypair operationalCertificate:(MTRCertificateDERBytes) operationalCertificate intermediateCertificate:(MTRCertificateDERBytes) intermediateCertificate rootCertificate:(MTRCertificateDERBytes) rootCertificate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerexternalcertificateparameters/init(storagedelegate:storagedelegatequeue:uniqueidentifier:ipk:vendorid:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:))*