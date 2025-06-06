# setupPanelShouldHandleMediaReservations(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

This delegate method allows the delegate to control how media reservations are handled.

**Availability**:
- macOS ?+

## Declaration

```swift
func setupPanelShouldHandleMediaReservations(_ aPanel: DRSetupPanel!) -> Bool
```

#### Return Value

#### Discussion

Return `NO` to indicate the delegate will handle media reservations. Return `YES` to indicate the setupPanel should handle media reservations itself.

## Parameters

- `aPanel`: The setup panel sending the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations(_:))*