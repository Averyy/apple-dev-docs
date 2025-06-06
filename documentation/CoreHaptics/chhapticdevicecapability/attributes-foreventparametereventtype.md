# attributes(forEventParameter:eventType:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Returns the haptic device’s attributes for an event parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func attributes(forEventParameter inParameter: CHHapticEvent.ParameterID, eventType type: CHHapticEvent.EventType) throws -> any CHHapticParameterAttributes
```

#### Return Value

The haptic device’s attributes for the given event parameter ID.

## Parameters

- `inParameter`: The event parameter ID whose attributes you seek.
- `type`: A haptic event type to query.

## See Also

- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](chhapticdevicecapability/attributes(fordynamicparameter:).md)
  Requests the haptic device’s attributes for a dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdevicecapability/attributes(foreventparameter:eventtype:))*