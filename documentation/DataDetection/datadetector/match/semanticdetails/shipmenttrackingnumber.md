# DataDetector.Match.SemanticDetails.ShipmentTrackingNumber

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents a shipment tracking number.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ShipmentTrackingNumber
```

#### Discussion

The [`carrier`](./shipmenttrackingnumber/carrier.md) property is a string that represents the carrier or service name, and the [`trackingNumber`](./shipmenttrackingnumber/trackingnumber.md) is the number used by the carrier to track the package. The [`trackingURL`](./shipmenttrackingnumber/trackingurl.md) may contain a URL that someone can use to track the progress of the delivery.

## Topics

### Properties that describe a shipment
- [let carrier: String](./shipmenttrackingnumber/carrier.md)
  A string that represents the carrier or service name.
- [let trackingNumber: String](./shipmenttrackingnumber/trackingnumber.md)
  The number the carrier uses to track the package.
- [let trackingURL: URL?](./shipmenttrackingnumber/trackingurl.md)
  A property that may contain a URL that someone can use to track the progress of the delivery.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/shipmenttrackingnumber)*