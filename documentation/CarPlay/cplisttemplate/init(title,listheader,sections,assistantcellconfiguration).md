# init(title:listHeader:sections:assistantCellConfiguration:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list template with a title, sections, and a header and assistant cell with optional details.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(title: String?, listHeader: CPListTemplateDetailsHeader?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title listHeader:(CPListTemplateDetailsHeader *) listHeader sections:(NSArray<CPListSection *> *) sections assistantCellConfiguration:(CPAssistantCellConfiguration *) assistantCellConfiguration;
```

## Return Value

A newly initialized list template.

## Discussion

If you add grid buttons to your list using the [`headerGridButtons`](./headergridbuttons.md) property, the grid buttons appear below the header section.

## Parameters

- `title`: The text to display in the navigation bar while the template is visible.
- `listHeader`: The header section to display above the list of items.
- `sections`: An array of sections, each with zero or more items. This initializer copies the array, trimming sections and items as needed to fit within the limits in the [`maximumSectionCount`](./maximumsectioncount.md) and [`maximumItemCount`](./maximumitemcount.md) properties. The initializer trims sections from the end of the array, and keeps adding items section by section until it reaches the maximum.
- `assistantCellConfiguration`: The configuration attributes for the assistant cell. Audio, video, and communication apps use this cell to facilitate interactions with Siri. Specify `nil` for all other types of apps.

## See Also

### Creating a list template
- [init(title: String?, sections: [CPListSection])](./init%28title,sections%29.md)
  Creates a list template with a title and sections to display.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and an assistant cell.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?, headerGridButtons: [CPGridButton]?)](./init%28title,sections,assistantcellconfiguration,headergridbuttons%29.md)
  Creates a list template with a title, sections, an optional assistant cell, and one or more buttons to display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:listheader:sections:assistantcellconfiguration:))*