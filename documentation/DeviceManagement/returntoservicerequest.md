# ReturnToServiceRequest

**Framework**: Device Management  
**Kind**: dictionary

The return-to-service request details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
object ReturnToServiceRequest
```

## Properties

- `MessageType` (string) *(required)*: The message type, which requires a value of `ReturnToService`.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.

## See Also

- [object ReturnToServiceResponse](returntoserviceresponse.md)
  The return-to-service response details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/returntoservicerequest)*