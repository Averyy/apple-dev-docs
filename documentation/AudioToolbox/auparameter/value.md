# value

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The parameter’s current value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var value: AUValue { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) AUValue value;
```

*macOS*

```objc
@property (atomic) AUValue value;
```

## See Also

### Managing Parameter Values
- [func setValue(AUValue, originator: AUParameterObserverToken?)](./setvalue%28_,originator%29.md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](./setvalue%28_,originator,athosttime%29.md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](./setvalue%28_,originator,athosttime,eventtype%29.md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](./string%28fromvalue%29.md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](./value%28from%29.md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/value)*