# nationalIDCardData(region:retaining:notRetaining:)

**Framework**: ProximityReader  
**Kind**: method

A request which retrieves elements from the holder and returns the validated document elements.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
static func nationalIDCardData(region: Locale.Region, retaining retainedElements: [MobileNationalIDCardDataRequest.Element] = [], notRetaining nonRetainedElements: [MobileNationalIDCardDataRequest.Element] = []) -> Self
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest/nationalidcarddata(region:retaining:notretaining:))*