# init(parameterID:value:relativeTime:)

**Framework**: Core Haptics  
**Kind**: init

Creates a dynamic parameter from its ID, value, and start time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(parameterID: CHHapticDynamicParameter.ID, value: Float, relativeTime time: TimeInterval)
```

## Parameters

- `parameterID`: The ID indicating the type of the dynamic parameter.
- `value`: The value of the dynamic parameter.
- `time`: The time at which to send the dynamic parameter.

## See Also

- [CHHapticDynamicParameter.ID](chhapticdynamicparameter/id.md)
  The identifier that reveals the type of property associated with a dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter/init(parameterid:value:relativetime:))*