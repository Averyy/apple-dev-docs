# outerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The outer text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var outerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * outerTextProvider;
```

## Discussion

The complication ignores the text provider’s tint color. It always displays the outer text as white.

## See Also

### Setting the Complication Data
- [var innerTextProvider: CLKTextProvider](./innertextprovider.md)
  The inner text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext/outertextprovider)*