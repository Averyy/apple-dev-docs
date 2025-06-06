# inputModes

**Framework**: SensorKit  
**Kind**: property

The active keyboard languages in the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var inputModes: [String] { get }
```

#### Discussion

An example array entry is `en_US`. A user may switch between multiple languages in the same session.

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
- [var sessionIdentifiers: [String]](srkeyboardmetrics/sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/inputmodes)*