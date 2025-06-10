# options

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

Customizations for a tip.

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
@Tips
.OptionsBuilder var options: [any TipOption] { get }
```

## See Also

- [typealias Option](tip/option.md)
  A type that represents the various customizations that you can make to a tip’s behavior.
- [typealias IgnoresDisplayFrequency](tip/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [typealias MaxDisplayCount](tip/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [typealias MaxDisplayDuration](tip/maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/options)*