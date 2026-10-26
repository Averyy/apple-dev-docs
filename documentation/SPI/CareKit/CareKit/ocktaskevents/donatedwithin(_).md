---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/donatedwithin(_:)"
framework: "CareKit/CareKit"
---

# donatedWithin(_:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.donatedWithin(_:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func donatedWithin<DonationInfo>(_ timeRange: Tips.DonationTimeRange) -> [Self.Element] where DonationInfo : Decodable, DonationInfo : Encodable, DonationInfo : Sendable, Self.Element == Tips.Event<DonationInfo>.Donation
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/donatedwithin(_:))*