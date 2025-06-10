# stage

**Framework**: EnergyKit  
**Kind**: property

An indirect measurement of power consumption by an HVAC electric heating or cooling stage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
let stage: Int
```

#### Discussion

An integer ranging from `0` to `100` that’s proportional to the amount of power consumed, where `0` and `100` correspond to the min and max power levels respectively.

- `0`: idle or off
- `100`: max.

Higher numbers mean more power.

For single stage systems, or devices which can’t provide `0-100`, `100` is acceptable as an indicator of active power consumption

For multi stage or variable speed systems, you should map stages based on their relative power consumption

## See Also

- [init(stage: Int)](electrichvacloadevent/electricalmeasurement/init(stage:).md)
  Initializes an electrical measurement for the electrical load event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/electricalmeasurement/stage)*