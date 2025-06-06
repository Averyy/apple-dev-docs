# valueChangedHandler

**Framework**: Game Controller  
**Kind**: property

The block that the profile calls when an element’s value changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var valueChangedHandler: GCExtendedGamepadValueChangedHandler? { get set }
```

#### Discussion

If multiple elements change values at the same time, the profile calls this block once for each element that changes. If the value of a subelement changes, the profile only calls the block for the containing element.

## See Also

- [typealias GCExtendedGamepadValueChangedHandler](gcextendedgamepadvaluechangedhandler.md)
  The signature for the block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/valuechangedhandler)*