# inputModes

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The active keyboard languages in the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var inputModes: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * inputModes;
```

#### Discussion

An example array entry is `en_US`. A user may switch between multiple languages in the same session.

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
- [var sessionIdentifiers: [String]](./sessionidentifiers.md)
  The identifiers for the keyboard sessions that report metrics to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/inputmodes)*