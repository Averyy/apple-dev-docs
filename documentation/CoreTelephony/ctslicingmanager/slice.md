# CTSlicingManager.Slice

**Framework**: Core Telephony  
**Kind**: struct  
**Role**: Structure

Information about an active network slice.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
struct Slice
```

## Overview

A `Slice` represents an active network slice configuration, including the app category it serves, the traffic class it uses, and the network interface handling the traffic.

Use the [`activeSlices`](./activeslices.md) property to retrieve information about currently active slices on the device.

## Topics

### Representing slice properties
- [let appCategory: CTSlicingManager.AppCategory](./slice/appcategory.md)
  An application category associated with this network slice.
- [let trafficClass: CTSlicingManager.TrafficClass?](./slice/trafficclass.md)
  A traffic class that routes traffic through this network slice.
- [let networkInterfaceName: String](./slice/networkinterfacename.md)
  A network interface name associated with the slice.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/slice)*