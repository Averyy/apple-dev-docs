# NSLevelIndicatorCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

`NSLevelIndicatorCell` is a subclass of [`NSActionCell`](./nsactioncell.md) that provides several level indicator display styles including: capacity, ranking and relevancy. The capacity style provides both continuous and discrete modes.

**Availability**:
- macOS

## Declaration

```swift
class NSLevelIndicatorCell
```

```objc
@interface NSLevelIndicatorCell : NSActionCell
```

## Topics

### Initializing NSLevelIndicatorCell Objects
- [init(levelIndicatorStyle: NSLevelIndicator.Style)](./nslevelindicatorcell/init%28levelindicatorstyle%29.md)
  Initializes the receiver with the style specified by `levelIndicatorStyle`.
### Configuring the Range of Values
- [var minValue: Double](./nslevelindicatorcell/minvalue.md)
  The minimum value of the control.
- [var maxValue: Double](./nslevelindicatorcell/maxvalue.md)
  The maximum value of the control.
- [var levelIndicatorStyle: NSLevelIndicator.Style](./nslevelindicatorcell/levelindicatorstyle.md)
  The style of the level indicator control.
- [var warningValue: Double](./nslevelindicatorcell/warningvalue.md)
  The warning value of the level indicator control.
- [var criticalValue: Double](./nslevelindicatorcell/criticalvalue.md)
  The critical value of the level indicator control.
### Managing Tick Marks
- [var tickMarkPosition: NSSlider.TickMarkPosition](./nslevelindicatorcell/tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](./nslevelindicatorcell/numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](./nslevelindicatorcell/numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](./nslevelindicatorcell/tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](./nslevelindicatorcell/rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).
### Constants
- [NSLevelIndicator.Style](./nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.

## Relationships

### Inherits From
- [NSActionCell](./nsactioncell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell)*