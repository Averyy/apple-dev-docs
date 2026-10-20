# innerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The inner text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var innerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * innerTextProvider;
```

#### Discussion

This property supports multicolor text.

## See Also

### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](./outertextprovider.md)
  The outer text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext/innertextprovider)*