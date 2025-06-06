# nationalIDCardRawData(region:retaining:notRetaining:)

**Framework**: ProximityReader  
**Kind**: method

A request which retrieves mobile national ID card elements from the holder and returns the raw response data for processing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
static func nationalIDCardRawData(region: Locale.Region, retaining retainedElements: [MobileNationalIDCardRawDataRequest.Element] = [], notRetaining nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element] = []) -> Self
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/nationalidcardrawdata(region:retaining:notretaining:))*