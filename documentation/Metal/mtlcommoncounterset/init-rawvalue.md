# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a common counter set name from a raw value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

Use one of the [`MTLCommonCounterSet`](mtlcommoncounterset.md) type’s static properties, such as [`timestamp`](mtlcommoncounterset/timestamp.md), [`stageUtilization`](mtlcommoncounterset/stageutilization.md), and [`statistic`](mtlcommoncounterset/statistic.md) instead of creating a common counter set instance yourself with this initializer.

## Parameters

- `rawValue`: The name of a counter set as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounterset/init(rawvalue:))*