# init(title:sections:assistantCellConfiguration:)

**Framework**: CarPlay  
**Kind**: init

Creates a sectioned list template that optionally displays the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)
```

#### Discussion

The system provides the text and accessory image for the assistant cell and you can’t change these. Use the [`assistantCellConfiguration`](cplisttemplate/assistantcellconfiguration.md) property to update the cell’s configuration after you initialize the template. CarPlay observes this property and automatically updates your app’s interface in response to any changes.

Your app doesn’t receive a callback when the user selects the assistant cell. Instead, you configure an Intents Extension to handle the type of intent you specify in the cell’s configuration; audio apps must support doc://com.apple.documentation/documentation/sirikit/inplaymediaintent and communication apps must support doc://com.apple.documentation/documentation/sirikit/instartcallintent.

## Parameters

- `title`: The title that the navigation bar displays while the template is visible.
- `sections`: An array of sections, each with zero or more list items. For more information, see  .
- `assistantCellConfiguration`: The object that provides the configuration attributes for the assistant cell, such as position and visibility. For more information, see  .

## See Also

- [init(title: String?, sections: [CPListSection])](cplisttemplate/init(title:sections:).md)
  Creates a list template with an array of list sections and optional title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:assistantcellconfiguration:))*