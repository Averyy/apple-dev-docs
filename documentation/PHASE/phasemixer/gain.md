# gain

**Framework**: PHASE  
**Kind**: property

The mixer’s volume.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gain: Double { get }
```

#### Discussion

The framework clamps the value to the range between `0` and `1`, where `0` silences the mixer’s volume and `1` doesn’t modify the volume.

## See Also

- [var gainMetaParameter: PHASEMetaParameter?](phasemixer/gainmetaparameter.md)
  A parameter that changes the mixer’s volume gradually over a period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixer/gain)*