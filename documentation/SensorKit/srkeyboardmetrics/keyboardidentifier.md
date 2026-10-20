# keyboardIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the keyboard in the keyboard list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var keyboardIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * keyboardIdentifier;
```

## See Also

### Inspecting Keyboard Configuration and Sessions
- [var duration: TimeInterval](./duration.md)
  The duration that the report spans.
- [var version: String](./version.md)
  The version of keyboard metrics.
- [var width: Measurement<UnitLength>](./width.md)
  The width, in millimeters, of the keyboard in the report.
- [var height: Measurement<UnitLength>](./height.md)
  The height, in millimeters, of the keyboard in the report.
- [var inputModes: [String]](./inputmodes.md)
  The active keyboard languages in the session.
- [var sessionIdentifiers: [String]](./sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/keyboardidentifier)*