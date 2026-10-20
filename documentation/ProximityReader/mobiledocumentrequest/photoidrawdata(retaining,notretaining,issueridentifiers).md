# photoIDRawData(retaining:notRetaining:issuerIdentifiers:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Type Method

A request which retrieves photo ID elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
static func photoIDRawData(retaining retainedElements: [MobilePhotoIDRawDataRequest.Element] = [], notRetaining nonRetainedElements: [MobilePhotoIDRawDataRequest.Element] = [], issuerIdentifiers: [Data] = []) -> Self
```

Available when `Self` is `MobilePhotoIDRawDataRequest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/photoidrawdata(retaining:notretaining:issueridentifiers:))*