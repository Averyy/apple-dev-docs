# isProducedByAccessory

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether the system receives the location from an external accessory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isProducedByAccessory: Bool { get }
```

#### Discussion

Core Location sets [`isProducedByAccessory`](cllocationsourceinformation/isproducedbyaccessory.md) to `true` if the system retrieved the location from an external accessory attached to the device, such as a Made for iPhone GPS dongle or CarPlay. Otherwise, the default value is `false`.

## See Also

- [var isSimulatedBySoftware: Bool](cllocationsourceinformation/issimulatedbysoftware.md)
  A Boolean value that indicates whether the system generates the location using on-device software simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationsourceinformation/isproducedbyaccessory)*