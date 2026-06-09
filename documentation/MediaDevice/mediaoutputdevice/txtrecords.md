# txtRecords

**Framework**: Media Device  
**Kind**: property

TXT records associated with the device discovered via network protocols.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let txtRecords: [NWTXTRecord]
```

#### Discussion

Contains key-value pairs of metadata about the device that were advertised during network discovery (for example, via Bonjour/mDNS). This information can include device-specific attributes, service capabilities, version information, or other properties that help identify and configure the connection.

> **Note**: `NWTXTRecord` for details on working with TXT record data


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/txtrecords)*