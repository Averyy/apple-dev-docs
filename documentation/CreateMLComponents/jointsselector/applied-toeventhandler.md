# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Select joints to be included in the pose. Ignored joints will be reset to zero in all fields.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to input: Pose, eventHandler: EventHandler? = nil) -> Pose
```

#### Return Value

A pose with the ignored joints set to zero.

## Parameters

- `input`: A pose.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/jointsselector/applied(to:eventhandler:))*