# init(title:sections:assistantCellConfiguration:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list template with a title, sections, and an assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title sections:(NSArray<CPListSection *> *) sections assistantCellConfiguration:(CPAssistantCellConfiguration *) assistantCellConfiguration;
```

## Return Value

A newly initialized list template.

## Discussion

The system provides the text and accessory image for the assistant cell; you can’t change these. Use the [`assistantCellConfiguration`](./assistantcellconfiguration.md) property to update the cell’s configuration after you initialize the template. CarPlay observes this property and automatically updates your app’s interface in response to any changes.

Your app doesn’t receive a callback when the user selects the assistant cell. Instead, you configure an Intents extension to handle the type of intent you specify in the cell’s configuration; audio apps must support [`INPlayMediaIntent`](../../Intents/inplaymediaintent.md) and communication apps must support [`INStartCallIntent`](../../Intents/instartcallintent.md).

## Parameters

- `title`: The text to display in the navigation bar while the template is visible.
- `sections`: An array of sections, each with zero or more items. This initializer copies the array, trimming sections and items as needed to fit within the limits in the [`maximumSectionCount`](./maximumsectioncount.md) and [`maximumItemCount`](./maximumitemcount.md) properties. The initializer trims sections from the end of the array, and keeps adding items section by section until it reaches the maximum.
- `assistantCellConfiguration`: The configuration attributes for the assistant cell. Audio, video, and communication apps use this cell to facilitate interactions with Siri. Specify `nil` for all other types of apps.

## See Also

### Creating a list template
- [init(title: String?, sections: [CPListSection])](./init%28title,sections%29.md)
  Creates a list template with a title and sections to display.
- [init(title: String?, listHeader: CPListTemplateDetailsHeader?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,listheader,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and a header and assistant cell with optional details.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?, headerGridButtons: [CPGridButton]?)](./init%28title,sections,assistantcellconfiguration,headergridbuttons%29.md)
  Creates a list template with a title, sections, an optional assistant cell, and one or more buttons to display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:assistantcellconfiguration:))*