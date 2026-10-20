# sessionIdentifiers

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The identifiers for the keyboard sessions that report metrics to the sample.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sessionIdentifiers: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * sessionIdentifiers;
```

#### Discussion

A keyboard session begins when the system presents the keyboard and ends when the system dismisses it.

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
- [var height: Measurement<UnitLength>](./height.md)
  The height, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](./inputmodes.md)
  The active keyboard languages in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sessionidentifiers)*