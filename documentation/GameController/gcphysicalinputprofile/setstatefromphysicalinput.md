# setStateFromPhysicalInput(_:)

**Framework**: Game Controller  
**Kind**: method

Copies the input values from a specified physical input profile to a snapshot of the profile.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setStateFromPhysicalInput(_ physicalInput: GCPhysicalInputProfile)
```

#### Discussion

If the associated controller isn’t a snapshot, this method does nothing.

## Parameters

- `physicalInput`: The physical input profile to copy the input values from.

## See Also

- [var isSnapshot: Bool](gccontroller/issnapshot.md)
  A Boolean value that indicates whether the controller is a snapshot of a controller.
- [func capture() -> Self](gcphysicalinputprofile/capture.md)
  Returns a snapshot of the profile with its current element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/setstatefromphysicalinput(_:))*