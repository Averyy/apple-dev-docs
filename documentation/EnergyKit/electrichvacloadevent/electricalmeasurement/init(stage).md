# init(stage:)

**Framework**: EnergyKit  
**Kind**: init  
**Role**: Initializer

Initializes an electrical measurement for the electrical load event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
init(stage: Int)
```

## Parameters

- `stage`: `0` indicates that the electrical device is idle. `100` indicates that it’s consuming or generating the most power possible.

## See Also

### Initializing an electrical measurement
- [let stage: Int](./stage.md)
  An indirect measurement of power consumption by an HVAC electric heating or cooling stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/electricalmeasurement/init(stage:))*