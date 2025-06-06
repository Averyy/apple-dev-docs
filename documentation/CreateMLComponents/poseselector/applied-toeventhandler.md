# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Select a pose if multiple poses are detected on the same frame.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to input: [Pose], eventHandler: EventHandler? = nil) -> Pose
```

#### Return Value

A selected pose based on the strategy.

## Parameters

- `input`: An array of poses.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/poseselector/applied(to:eventhandler:))*