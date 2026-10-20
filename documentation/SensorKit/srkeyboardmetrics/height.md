# height

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The height, in millimeters, of the keyboard in the report.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var height: Measurement<UnitLength> { get }
```

```objc
@property (readonly) NSMeasurement<NSUnitLength *> * height;
```

## See Also

### Inspecting Keyboard Configuration and Sessions
- [var duration: TimeInterval](./duration.md)
  The duration that the report spans.
- [var keyboardIdentifier: String](./keyboardidentifier.md)
  The identifier of the keyboard in the keyboard list.
- [var version: String](./version.md)
  The version of keyboard metrics.
- [var width: Measurement<UnitLength>](./width.md)
  The width, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](./inputmodes.md)
  The active keyboard languages in the session.
- [var sessionIdentifiers: [String]](./sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/height)*