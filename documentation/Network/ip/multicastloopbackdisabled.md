# multicastLoopbackDisabled(_:)

**Framework**: Network  
**Kind**: method

Specify if multicast packets should be looped back for local delivery.

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
func multicastLoopbackDisabled(_ disableMulticastLoopback: Bool) -> IP
```

#### Discussion

By default, a multicast packet sent to a group to which the sending host itself belongs will be looped back for local delivery. `disableMulticastLoopback` disables this behavior and, if set, multicast packets will not be looped back to the sender.

> **Note**: Only applies to multicast packets.

## Parameters

- `disableMulticastLoopback`: True to disable multicast loopback, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip/multicastloopbackdisabled(_:))*