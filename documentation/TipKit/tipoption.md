# Option

**Framework**: TipKit  
**Kind**: protocol

A type that represents the various customizations that you can make to a tip’s behavior.

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
protocol TipOption : Sendable
```

## Topics

### Tip options
- [typealias IgnoresDisplayFrequency](tip/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [typealias MaxDisplayCount](tip/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [typealias MaxDisplayDuration](tip/maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [IgnoresDisplayFrequency](tips/ignoresdisplayfrequency.md)
- [MaxDisplayCount](tips/maxdisplaycount.md)
- [MaxDisplayDuration](tips/maxdisplayduration.md)

## See Also

- [struct AnyTip](anytip.md)
  A type-erased tip value.
- [struct TipKitError](tipkiterror.md)
  A localized tip kit error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipoption)*