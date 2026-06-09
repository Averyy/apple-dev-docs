# inputState(forSpatialAccessoryAnchorTimestamp:)

**Framework**: Game Controller  
**Kind**: method  
**Required**: Yes

Returns the buffered input state that best aligns with the provided spatial accessory anchor timestamp.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
func inputState(forSpatialAccessoryAnchorTimestamp timestamp: TimeInterval) -> (any GCDevicePhysicalInputState)?
```

#### Return Value

The buffered accessory input state that most closely aligns with the provided spatial accessory anchor timestamp.

## Parameters

- `timestamp`: The timestamp obtained from `ar_accessory_anchor_get_timestamp` for a spatial accessory anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/inputstate(forspatialaccessoryanchortimestamp:))*