# ReturnToServiceResponse

**Framework**: Device Management  
**Kind**: dictionary

The return-to-service response details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ReturnToServiceResponse
```

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

## Topics

### Objects
- [object ReturnToServiceResponse.ReturnToService](returntoserviceresponse/returntoservice-data.dictionary.md)
  A dictionary containing the configuration for return to service.

## Properties

- `PreserveDataPlan` (boolean): If `true`, the device preserves the data plan on an iPhone or iPad with eSIM functionality, if one exists. This value is available in iOS 26.4 and later.
- `ReturnToService` (ReturnToServiceResponse.ReturnToService) *(required)*: A dictionary containing the configuration for return to service.

## See Also

- [object ReturnToServiceRequest](returntoservicerequest.md)
  The return-to-service request details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/returntoserviceresponse)*