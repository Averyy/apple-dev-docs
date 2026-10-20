# setValue(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Sets the normalized value of the axis.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Float)
```

```objc
- (void) setValue:(float) value;
```

## Parameters

- `value`: A normalized value ranging from `-1` to `1` where `0` is in the dead zone.

## See Also

### Accessing the input values
- [var value: Float](./value.md)
  The current value of the axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/setvalue(_:))*