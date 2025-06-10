# init(storageDelegate:storageDelegateQueue:uniqueIdentifier:ipk:vendorID:operationalKeypair:operationalCertificate:intermediateCertificate:rootCertificate:)

**Framework**: Matter  
**Kind**: init

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerexternalcertificateparameters/init(storagedelegate:storagedelegatequeue:uniqueidentifier:ipk:vendorid:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:))*