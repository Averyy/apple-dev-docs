# capture()

**Framework**: Game Controller  
**Kind**: method

Returns a snapshot of the profile with its current element values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func capture() -> Self
```

#### Return Value

A snapshot of the profile.

#### Discussion

A snapshot is a copy of profile at a moment in time with its current element values. Unlike other profiles, you can set the values of a snapshot’s elements.

## See Also

- [func setStateFromPhysicalInput(GCPhysicalInputProfile)](gcphysicalinputprofile/setstatefromphysicalinput(_:).md)
  Copies the input values from a specified physical input profile to a snapshot of the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/capture())*