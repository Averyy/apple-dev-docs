# levelIndicatorStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style of the level indicator control.

**Availability**:
- macOS

## Declaration

```swift
var levelIndicatorStyle: NSLevelIndicator.Style { get set }
```

```objc
@property NSLevelIndicatorStyle levelIndicatorStyle;
```

#### Discussion

The style determines the default minimum and maximum values of the control. For a list of possible styles, see [`NSLevelIndicator.Style`](../nslevelindicator/style.md).

## See Also

### Configuring the Range of Values
- [var minValue: Double](./minvalue.md)
  The minimum value of the control.
- [var maxValue: Double](./maxvalue.md)
  The maximum value of the control.
- [var warningValue: Double](./warningvalue.md)
  The warning value of the level indicator control.
- [var criticalValue: Double](./criticalvalue.md)
  The critical value of the level indicator control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/levelindicatorstyle)*