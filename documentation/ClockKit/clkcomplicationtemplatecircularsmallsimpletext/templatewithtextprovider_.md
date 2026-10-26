# templateWithTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template from the provided text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithTextProvider:(CLKTextProvider *) textProvider;
```

## Parameters

- `textProvider`: A text provider for the text in the center of the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(textProvider: CLKTextProvider)](./init%28textprovider%29.md)
  Creates a new template from the provided text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallsimpletext/templatewithtextprovider:)*