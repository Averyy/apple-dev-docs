# init(relativeTime:value:)

**Framework**: Core Haptics  
**Kind**: init  
**Role**: Initializer

Creates a control point from its time and value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(relativeTime time: TimeInterval, value: Float)
```

```objc
- (instancetype) initWithRelativeTime:(NSTimeInterval) time value:(float) value;
```

## Parameters

- `time`: The time at which the associated parameter reaches this value, relative to the parameter curve’s start time.
- `value`: The value of the parameter at this control point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve/controlpoint/init(relativetime:value:))*