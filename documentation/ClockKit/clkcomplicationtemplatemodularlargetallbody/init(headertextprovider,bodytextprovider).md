# init(headerTextProvider:bodyTextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a template that has a header and a row of tall body text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(headerTextProvider: CLKTextProvider, bodyTextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithHeaderTextProvider:(CLKTextProvider *) headerTextProvider bodyTextProvider:(CLKTextProvider *) bodyTextProvider;
```

## Parameters

- `headerTextProvider`: The text provider for the header. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `bodyTextProvider`: The text provider for the body. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody/init(headertextprovider:bodytextprovider:))*