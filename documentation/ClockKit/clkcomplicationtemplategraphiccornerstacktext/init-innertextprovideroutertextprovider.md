# init(innerTextProvider:outerTextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a template that has an inner line of text and an outer text element.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(innerTextProvider: CLKTextProvider, outerTextProvider: CLKTextProvider)
```

## Parameters

- `innerTextProvider`: The text provider for the inner line of text. The template supports multicolored text from this text provider.
- `outerTextProvider`: The text provider for the outer line of text. The template ignores this text provider’s tint color, and always displays the text with a system color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext/init(innertextprovider:outertextprovider:))*