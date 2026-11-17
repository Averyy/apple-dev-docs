# headerGridButtons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Buttons to display in the header area above the list content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var headerGridButtons: [CPGridButton]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<CPGridButton *> * headerGridButtons;
```

## Discussion

The list displays these buttons below the header in [`listHeader`](./listheader.md) and above the items in the list. If you modify this property when the list is visible, CarPlay automatically refreshes the appearance of the header to reflect the new content.

## See Also

### Managing the supplemental content
- [var title: String?](./title.md)
  The title to display in the navigation bar when the list is visible.
- [var listHeader: CPListTemplateDetailsHeader?](./listheader.md)
  An optional header to display between the navigation bar and first section of content.
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](./assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/headergridbuttons)*