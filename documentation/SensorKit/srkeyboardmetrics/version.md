# version

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The version of keyboard metrics.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var version: String { get }
```

```objc
@property (copy, readonly) NSString * version;
```

## See Also

### Inspecting Keyboard Configuration and Sessions
- [var duration: TimeInterval](./duration.md)
  The duration that the report spans.
- [var keyboardIdentifier: String](./keyboardidentifier.md)
  The identifier of the keyboard in the keyboard list.
- [var width: Measurement<UnitLength>](./width.md)
  The width, in millimeters, of the keyboard in the report.
- [var height: Measurement<UnitLength>](./height.md)
  The height, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](./inputmodes.md)
  The active keyboard languages in the session.
- [var sessionIdentifiers: [String]](./sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/version)*