# init(title:sections:buttonConfiguration:)

**Framework**: CarPlay  
**Kind**: init

Creates and configures a new map panel for display over your navigation app’s map template.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(title: String?, sections: [CPMapPanelSection], buttonConfiguration: CPMapPanelButtonConfiguration?)
```

#### Return Value

A new map panel instance.

## Parameters

- `title`: The title of the map panel. This title appears at the top of the panel display. The panel stores a copy of the string you provide.
- `sections`: The information to display in the panel. Use this parameter to specify route options, charging stations, or other relevant content. If the number of items in this array exceeds the value in the [`maximumPanelItemsCount`](cppanel/maximumpanelitemscount.md) property, the map panel ignores any array items past the maximum. The system stores a copy of the array you provide.
- `buttonConfiguration`: Optional buttons and travel estimate data to display at the bottom of the panel. Specify `nil` if you don’t want to include any buttons in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/init(title:sections:buttonconfiguration:))*