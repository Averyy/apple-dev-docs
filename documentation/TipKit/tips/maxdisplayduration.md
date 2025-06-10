# MaxDisplayDuration

**Framework**: TipKit  
**Kind**: struct

Specifies the maximum amount of time a tip is displayed before it is invalidated.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MaxDisplayDuration
```

#### Overview

Use this option to automatically invalidate a tip after it has been displayed for a specified time interval.

This is a cumulative value; if a tip specifies a 2 minute maximum display duration and is displayed for 1 minute on Monday and 1 minute on Tuesday it will be automatically invalidated and no longer appear.

Tip views have a minimum display duration of 60 seconds before they can be automatically invalidated by `MaxDisplayDuration` in order to avoid appearing and disappearing too quickly.

By default tips have no maximum display duration.

```swift
struct FavoriteBackyardTip: Tip {
    var options: [any Option] {
        // Tip will automatically be invalidated 
        // after it has been displayed for 5 minutes.
        MaxDisplayDuration(300.0)
    }
}
```

## Topics

### Initializers
- [init(TimeInterval)](tips/maxdisplayduration/init(_:).md)

## Relationships

### Conforms To
- [Option](tipoption.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IgnoresDisplayFrequency](tips/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [struct MaxDisplayCount](tips/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/maxdisplayduration)*