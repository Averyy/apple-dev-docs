# sessionIdentifiers

**Framework**: SensorKit  
**Kind**: property

The identifiers for the keyboard sessions that report metrics to the sample.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sessionIdentifiers: [String] { get }
```

#### Discussion

A keyboard session begins when the system presents the keyboard and ends when the system dismisses it.

## See Also

- [var duration: TimeInterval](srkeyboardmetrics/duration.md)
  The duration that the report spans.
- [var keyboardIdentifier: String](srkeyboardmetrics/keyboardidentifier.md)
  The identifier of the keyboard in the keyboard list.
- [var version: String](srkeyboardmetrics/version.md)
  The version of keyboard metrics.
- [var width: Measurement<UnitLength>](srkeyboardmetrics/width.md)
  The width, in millimeters, of the keyboard in the report.
- [var height: Measurement<UnitLength>](srkeyboardmetrics/height.md)
  The height, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](srkeyboardmetrics/inputmodes.md)
  The active keyboard languages in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers)*