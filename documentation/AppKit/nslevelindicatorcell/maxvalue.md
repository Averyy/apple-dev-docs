# maxValue

**Framework**: AppKit  
**Kind**: property

The maximum value of the control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var maxValue: Double { get set }
```

#### Discussion

The maximum value is dependent on the style of the control. For continuous styles, the default value of this property is `100.0`. For discrete styles, the default maximum value is `5.0`.

## See Also

- [var minValue: Double](nslevelindicatorcell/minvalue.md)
  The minimum value of the control.
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicatorcell/levelindicatorstyle.md)
  The style of the level indicator control.
- [var warningValue: Double](nslevelindicatorcell/warningvalue.md)
  The warning value of the level indicator control.
- [var criticalValue: Double](nslevelindicatorcell/criticalvalue.md)
  The critical value of the level indicator control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/maxvalue)*