# Tip.IgnoresDisplayFrequency

**Framework**: TipKit  
**Kind**: typealias

Controls whether a tip obeys the preconfigured display frequency interval.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
typealias IgnoresDisplayFrequency = Tips.IgnoresDisplayFrequency
```

#### Overview

Use this option to allow a tip to appear even if the [`displayFrequency(_:)`](tips/configurationoption/displayfrequency(_:).md) has not been satisfied.

The default value of this option is false.

```swift
struct FavoriteBackyardTip: Tip {
    var options: [any Option] {
        IgnoresDisplayFrequency(true)
    }
}
```

## See Also

- [typealias MaxDisplayCount](tip/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [typealias MaxDisplayDuration](tip/maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/ignoresdisplayfrequency)*