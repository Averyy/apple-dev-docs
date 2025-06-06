# outerTextProvider

**Framework**: ClockKit  
**Kind**: property

The outer text to display in the complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var outerTextProvider: CLKTextProvider { get set }
```

#### Discussion

The complication ignores the text provider’s tint color. It always displays the outer text as white.

## See Also

- [var innerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccornerstacktext/innertextprovider.md)
  The inner text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext/outertextprovider)*