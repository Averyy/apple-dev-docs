# init(title:sections:assistantCellConfiguration:headerGridButtons:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list template with a title, sections, an optional assistant cell, and one or more buttons to display in the header.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?, headerGridButtons: [CPGridButton]?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title sections:(NSArray<CPListSection *> *) sections assistantCellConfiguration:(CPAssistantCellConfiguration *) assistantCellConfiguration headerGridButtons:(NSArray<CPGridButton *> *) headerGridButtons;
```

## Return Value

A newly initialized list template.

## Discussion

If you add a header to your list using the [`listHeader`](./listheader.md) property, the header appears above the buttons in the `headerGridButtons` parameter.

## Parameters

- `title`: The text to display in the navigation bar while the template is visible.
- `sections`: An array of sections, each with zero or more items. This initializer copies the array, trimming sections and items as needed to fit within the limits in the [`maximumSectionCount`](./maximumsectioncount.md) and [`maximumItemCount`](./maximumitemcount.md) properties. The initializer trims sections from the end of the array, and keeps adding items section by section until it reaches the maximum.
- `assistantCellConfiguration`: The configuration attributes for the assistant cell. Audio, video, and communication apps use this cell to facilitate interactions with Siri. Specify `nil` for all other types of apps.
- `headerGridButtons`: An array of buttons to display in a header section at the top of the list. Use these buttons to specify common actions someone might perform.

## See Also

### Creating a list template
- [init(title: String?, sections: [CPListSection])](./init%28title,sections%29.md)
  Creates a list template with a title and sections to display.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and an assistant cell.
- [init(title: String?, listHeader: CPListTemplateDetailsHeader?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,listheader,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and a header and assistant cell with optional details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:assistantcellconfiguration:headergridbuttons:))*