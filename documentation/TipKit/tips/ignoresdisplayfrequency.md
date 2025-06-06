# Tips.IgnoresDisplayFrequency

**Framework**: TipKit  
**Kind**: struct

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
struct IgnoresDisplayFrequency
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

## Topics

### Initializers
- [init(Bool)](tips/ignoresdisplayfrequency/init(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [TipOption](tipoption.md)

## See Also

- [struct MaxDisplayCount](tips/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [struct ConfigurationOption](tips/configurationoption.md)
  A type that marks an object as a tip configuration.
- [struct ParameterOption](tips/parameteroption.md)
  A type that represents the various customizations that you can make to a tip parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/ignoresdisplayfrequency)*