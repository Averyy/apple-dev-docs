# forwardingStatus(for:)

**Framework**: Accessory Notifications  
**Kind**: method

Retrieves the current notification forwarding status for an accessory.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func forwardingStatus(for accessory: ASAccessory) async throws -> ForwardingDecision
```

#### Return Value

The current forwarding decision for the specified accessory.

## Parameters

- `accessory`: The accessory to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/forwardingstatus(for:))*