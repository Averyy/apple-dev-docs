# valueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property

The block that the profile calls when an element’s value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var valueDidChangeHandler: ((GCPhysicalInputProfile, GCControllerElement) -> Void)? { get set }
```

#### Discussion

The block’s parameters are:

If multiple elements change values at the same time, the profile calls this block once for each element that changes. If the value of a subelement changes, the profile only calls the block for the containing element.

## See Also

- [var lastEventTimestamp: TimeInterval](gcphysicalinputprofile/lasteventtimestamp.md)
  The time of the most recent change to an element’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/valuedidchangehandler)*