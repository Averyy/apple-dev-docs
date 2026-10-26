# init(textProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template from the provided text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(textProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithTextProvider:(CLKTextProvider *) textProvider;
```

## Parameters

- `textProvider`: The text provider for a single line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [+ templateWithTextProvider:](./templatewithtextprovider_.md)
  Returns a new template from the provided text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext/init(textprovider:))*