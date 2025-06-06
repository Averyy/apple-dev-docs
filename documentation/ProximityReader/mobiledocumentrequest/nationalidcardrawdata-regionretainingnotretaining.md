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

## See Also

- [struct MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest/nationalidcardrawdata(region:retaining:notretaining:))*