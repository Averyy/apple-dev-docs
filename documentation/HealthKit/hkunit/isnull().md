# isNull()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the unit is null.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isNull() -> Bool
```

```objc
- (BOOL) isNull;
```

## Return Value

[`true`](../../Swift/true.md) if the unit is null; otherwise, [`false`](../../Swift/false.md).

## Discussion

Null units occur only when you create compound units in which all the units cancel out. For example, if you tried to create a unit by dividing deciliters by liters (`dL/L`), you would end up with a null unit.

## See Also

### Working with units
- [convenience init(from: String)](./init%28from%29-9qont.md)
  Returns the unit instance described by the provided string.
- [var unitString: String](./unitstring.md)
  A string representation of the unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/isnull())*