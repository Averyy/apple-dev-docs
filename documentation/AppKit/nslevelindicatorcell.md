# NSLevelIndicatorCell

**Framework**: AppKit  
**Kind**: class

`NSLevelIndicatorCell` is a subclass of [`NSActionCell`](nsactioncell.md) that provides several level indicator display styles including: capacity, ranking and relevancy. The capacity style provides both continuous and discrete modes.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSLevelIndicatorCell
```

## Topics

### Initializing NSLevelIndicatorCell Objects
- [init(levelIndicatorStyle: NSLevelIndicator.Style)](nslevelindicatorcell/init(levelindicatorstyle:).md)
  Initializes the receiver with the style specified by `levelIndicatorStyle`.
### Configuring the Range of Values
- [var minValue: Double](nslevelindicatorcell/minvalue.md)
  The minimum value of the control.
- [var maxValue: Double](nslevelindicatorcell/maxvalue.md)
  The maximum value of the control.
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicatorcell/levelindicatorstyle.md)
  The style of the level indicator control.
- [var warningValue: Double](nslevelindicatorcell/warningvalue.md)
  The warning value of the level indicator control.
- [var criticalValue: Double](nslevelindicatorcell/criticalvalue.md)
  The critical value of the level indicator control.
### Managing Tick Marks
- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicatorcell/tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](nslevelindicatorcell/numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](nslevelindicatorcell/numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](nslevelindicatorcell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicatorcell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).
### Constants
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell)*