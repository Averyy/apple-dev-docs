# nationalIDCardRawData(region:retaining:notRetaining:issuerIdentifiers:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Type Method

A request which retrieves mobile national ID card elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
static func nationalIDCardRawData(region: Locale.Region, retaining retainedElements: [MobileNationalIDCardRawDataRequest.Element] = [], notRetaining nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element] = [], issuerIdentifiers: [Data] = []) -> Self
```

Available when `Self` is `MobileNationalIDCardRawDataRequest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/nationalidcardrawdata(region:retaining:notretaining:issueridentifiers:))*