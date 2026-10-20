# IgnoresDisplayFrequency

**Framework**: TipKit  
**Kind**: typealias  
**Role**: Type Alias

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

Use this option to allow a tip to appear even if the [`displayFrequency(_:)`](../tips/configurationoption/displayfrequency%28_%29.md) has not been satisfied.

The default value of this option is false.

```swift
struct FavoriteBackyardTip: Tip {
    var options: [any Option] {
        IgnoresDisplayFrequency(true)
    }
}
```

## See Also

### Customizing tip behavior
- [var options: [any TipOption]](./options.md)
  Customizations for a tip.
- [typealias Option](./option.md)
  A type that represents the various customizations that you can make to a tip’s behavior.
- [typealias MaxDisplayCount](./maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [typealias MaxDisplayDuration](./maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/ignoresdisplayfrequency)*