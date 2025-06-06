# init(textProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template from the provided text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(textProvider: CLKTextProvider)
```

## Parameters

- `textProvider`: The text provider for a single line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargesimpletext/init(textprovider:))*