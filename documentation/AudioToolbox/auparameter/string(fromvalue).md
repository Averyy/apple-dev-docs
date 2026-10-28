# string(fromValue:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Gets the string representation of a parameter value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func string(fromValue value: UnsafePointer<AUValue>?) -> String
```

```objc
- (NSString *) stringFromValue:(const AUValue *) value;
```

## Return Value

The string representation of a parameter value.

## Discussion

Pass `nil` into the `value` parameter to use the current value.

## Parameters

- `value`: The parameter value to represent as a string.

## See Also

### Managing Parameter Values
- [var value: AUValue](./value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](./setvalue%28_,originator%29.md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](./setvalue%28_,originator,athosttime%29.md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](./setvalue%28_,originator,athosttime,eventtype%29.md)
- [func value(from: String) -> AUValue](./value%28from%29.md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/string(fromvalue:))*