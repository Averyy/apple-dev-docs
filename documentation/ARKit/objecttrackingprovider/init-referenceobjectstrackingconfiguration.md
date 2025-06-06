# init(referenceObjects:trackingConfiguration:)

**Framework**: ARKit  
**Kind**: init

Creates an object-tracking provider.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(referenceObjects: [ReferenceObject], trackingConfiguration: ObjectTrackingProvider.TrackingConfiguration? = nil)
```

#### Discussion

The method clamps the numeric parameter values for configuring tracking if they’re outside their supported range.

## Parameters

- `referenceObjects`: The reference objects to look for
- `trackingConfiguration`: Optional parameters for configuring object tracking if not provided, the framework applies a set of default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/init(referenceobjects:trackingconfiguration:))*