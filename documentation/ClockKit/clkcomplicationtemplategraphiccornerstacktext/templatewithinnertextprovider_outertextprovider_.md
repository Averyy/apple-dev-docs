# templateWithInnerTextProvider:outerTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a template that has an inner line of text and an outer text element.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithInnerTextProvider:(CLKTextProvider *) innerTextProvider outerTextProvider:(CLKTextProvider *) outerTextProvider;
```

## Parameters

- `innerTextProvider`: The text provider for the inner line of text. The template supports multicolored text from this text provider.
- `outerTextProvider`: The text provider for the outer line of text. The template ignores this text provider’s tint color, and always displays the text with a system color.

## See Also

### Creating the Template
- [init(innerTextProvider: CLKTextProvider, outerTextProvider: CLKTextProvider)](./init%28innertextprovider,outertextprovider%29.md)
  Creates a template that has an inner line of text and an outer text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext/templatewithinnertextprovider:outertextprovider:)*