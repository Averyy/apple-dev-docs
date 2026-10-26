---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockstylable"
framework: "CareKit/CareKitUI"
---

# OCKStylable

**Framework**: CareKit/CareKitUI  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol OCKStylable
```

## Topics

### Instance Properties
- [var customStyle: OCKStyler?](./ockstylable/customstyle.md)
  Used to override the style.
### Instance Methods
- [func style() -> OCKStyler](./ockstylable/style%28%29.md)
  Returns in order of existence: This object’s custom style, the first parent with a custom style, or the default style.
- [func styleChildren()](./ockstylable/stylechildren%28%29.md)
  Notify this view and subviews that the style has changed. Guarantees that the outermost view’s `styleDidChange` method will be called after that of inner views.
- [func styleDidChange()](./ockstylable/styledidchange%28%29.md)
  Called when the style changes.

## Relationships

### Conforming Types
- [OCKAddressButton](./ockaddressbutton.md)
- [OCKAnimatedButton](./ockanimatedbutton.md)
- [OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
- [OCKCartesianChartView](./ockcartesianchartview.md)
- [OCKCartesianGraphView](./ockcartesiangraphview.md)
- [OCKChecklistItemButton](./ockchecklistitembutton.md)
- [OCKChecklistTaskView](./ockchecklisttaskview.md)
- [OCKCheckmarkButton](./ockcheckmarkbutton.md)
- [OCKCompletionRingButton](./ockcompletionringbutton.md)
- [OCKCompletionRingView](./ockcompletionringview.md)
- [OCKContactButton](./ockcontactbutton.md)
- [OCKDetailView](./ockdetailview.md)
- [OCKDetailedContactView](./ockdetailedcontactview.md)
- [OCKFeaturedContentView](./ockfeaturedcontentview.md)
- [OCKGridTaskView](./ockgridtaskview.md)
- [OCKHeaderView](./ockheaderview.md)
- [OCKInstructionsTaskView](./ockinstructionstaskview.md)
- [OCKLabel](./ocklabel.md)
- [OCKLabeledButton](./ocklabeledbutton.md)
- [OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
- [OCKLogItemButton](./ocklogitembutton.md)
- [OCKLogTaskView](./ocklogtaskview.md)
- [OCKSeparatorView](./ockseparatorview.md)
- [OCKSimpleContactView](./ocksimplecontactview.md)
- [OCKSimpleTaskView](./ocksimpletaskview.md)
- [OCKStackView](./ockstackview.md)
- [OCKView](./ockview.md)
- [OCKWeekCalendarView](./ockweekcalendarview.md)

## See Also

### Styles
- [struct OCKStyle](./ockstyle.md)
- [struct OCKAnimationStyle](./ockanimationstyle.md)
  Concrete object for animation constants.
- [struct OCKAppearanceStyle](./ockappearancestyle.md)
  Concrete object for appearance constants.
- [struct OCKColorStyle](./ockcolorstyle.md)
  Concrete object for color constants.
- [struct OCKDimensionStyle](./ockdimensionstyle.md)
  Concrete object for dimension constants.
- [protocol OCKStyler](./ockstyler.md)
  Defines styling constants.
- [protocol OCKAnimationStyler](./ockanimationstyler.md)
  Defines constants for values used during animations.
- [protocol OCKAppearanceStyler](./ockappearancestyler.md)
  Defines constants for view appearance styling.
- [protocol OCKColorStyler](./ockcolorstyler.md)
  Defines color constants.
- [protocol OCKDimensionStyler](./ockdimensionstyler.md)
  Defines constants for view dimension styling.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockstylable)*