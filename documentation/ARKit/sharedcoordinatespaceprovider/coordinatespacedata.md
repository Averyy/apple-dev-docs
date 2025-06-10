# SharedCoordinateSpaceProvider.CoordinateSpaceData

**Framework**: ARKit  
**Kind**: struct

A coordinate space data.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CoordinateSpaceData
```

#### Overview

The underlying data needs to be sent to each participant in the shared coordinate space.

## Topics

### Initializers
- [init?(data: Data)](sharedcoordinatespaceprovider/coordinatespacedata/init(data:).md)
  Initialize a `CoordinateSpaceData` from a Data blob received over network.
### Instance Properties
- [var data: Data](sharedcoordinatespaceprovider/coordinatespacedata/data.md)
  Extract a `Data` object to be transported over network.
- [var recipientIdentifiers: [UUID]](sharedcoordinatespaceprovider/coordinatespacedata/recipientidentifiers.md)
  Participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/sharedcoordinatespaceprovider/coordinatespacedata)*