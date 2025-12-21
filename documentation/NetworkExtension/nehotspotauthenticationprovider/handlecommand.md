# handleCommand(_:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Handles a given hotspot command, in response to a request from the framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func handleCommand(_ command: NEHotspotHelperCommand) async -> NEHotspotHelperResponse
```

#### Return Value

An [`NEHotspotHelperResponse`](nehotspothelperresponse.md) with the result of the call.

#### Discussion

In your implementation, handle the specified command and return an appropriate [`NEHotspotHelperResponse`](nehotspothelperresponse.md). The framework is responsible for delivering this response to the system; don’t invoke the [`deliver()`](nehotspothelperresponse/deliver().md) method of [`NEHotspotHelperResponse`](nehotspothelperresponse.md) manually.

## See Also

- [class NEHotspotHelperCommand](nehotspothelpercommand.md)
  A command for the hotspot helper to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationprovider/handlecommand(_:))*