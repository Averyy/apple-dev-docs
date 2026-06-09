# photoIDRawData(retaining:notRetaining:issuerIdentifiers:)

**Framework**: ProximityReader  
**Kind**: method

A request which retrieves photo ID elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func photoIDRawData(retaining retainedElements: [MobilePhotoIDRawDataRequest.Element] = [], notRetaining nonRetainedElements: [MobilePhotoIDRawDataRequest.Element] = [], issuerIdentifiers: [Data] = []) -> Self
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/photoidrawdata(retaining:notretaining:issueridentifiers:))*