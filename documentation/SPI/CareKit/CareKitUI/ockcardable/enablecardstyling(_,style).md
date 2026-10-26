---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcardable/enablecardstyling(_:style:)"
framework: "CareKit/CareKitUI"
---

# enableCardStyling(_:style:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Turn the card styling on/off. If this view is stylable, this method should be called from the `styleDidChange` method. Note that shadow rasterizing is set on by default, and consequently a shadow cannot be set over a clear background.

## Declaration

```swift
func enableCardStyling(_ enabled: Bool, style: OCKStyler)
```

## Parameters

- `enabled`: True to turn the card styling on.
- `style`: The style to use for the card.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcardable/enablecardstyling(_:style:))*