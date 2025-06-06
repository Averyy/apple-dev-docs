# Tips.MaxDisplayCount

**Framework**: TipKit  
**Kind**: struct

Specifies the maximum number of times a tip displays before the system automatically invalidates it.

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
struct MaxDisplayCount
```

#### Overview

Use this option to automatically invalidate a tip after it has appeared a specified number of times.

By default tips have no maximum display count.

```swift
struct FavoriteBackyardTip: Tip {
    var options: [any Option] {
        // Tip will only appear 3 times before it is automatically invalidated.
        MaxDisplayCount(3)
    }
}
```

## Topics

### Initializers
- [init(Int)](tips/maxdisplaycount/init(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [TipOption](tipoption.md)

## See Also

- [struct IgnoresDisplayFrequency](tips/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [struct ConfigurationOption](tips/configurationoption.md)
  A type that marks an object as a tip configuration.
- [struct ParameterOption](tips/parameteroption.md)
  A type that represents the various customizations that you can make to a tip parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/maxdisplaycount)*