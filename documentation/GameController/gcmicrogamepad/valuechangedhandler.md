# valueChangedHandler

**Framework**: Game Controller  
**Kind**: property

The block that this profile calls when an element’s value changes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var valueChangedHandler: GCMicroGamepadValueChangedHandler? { get set }
```

#### Discussion

If multiple elements change values at the same time, the profile calls this block once for each element that changed. If the value of a child element changes, the profile only calls the block for the containing element.

## See Also

- [typealias GCMicroGamepadValueChangedHandler](gcmicrogamepadvaluechangedhandler.md)
  Signature for the block that this profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/valuechangedhandler)*