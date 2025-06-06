# report(_:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method

Reports an event to the system.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func report(_ inEvent: DDDeviceEvent)
```

#### Discussion

The extension updates the system with the discovery status of the device of interest by passing event objects (`DDEvent`) through this function.

## Parameters

- `inEvent`: The event to report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoverysession/report(_:))*