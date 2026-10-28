# SharedCoordinateSpaceProvider.CoordinateSpaceData

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A coordinate space data object.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct CoordinateSpaceData
```

## Overview

> **Note**: The underlying data needs to be sent to each participant in the shared coordinate space.

## Topics

### Initializers
- [init?(data: Data)](./coordinatespacedata/init%28data%29.md)
  Initialize a `CoordinateSpaceData` from a data blob.
### Instance Properties
- [var data: Data](./coordinatespacedata/data.md)
  Extract a `Data` object.
- [var recipientIdentifiers: [UUID]](./coordinatespacedata/recipientidentifiers.md)
  Participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/sharedcoordinatespaceprovider/coordinatespacedata)*