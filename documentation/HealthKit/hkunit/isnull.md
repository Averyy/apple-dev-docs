# isNull()

**Framework**: HealthKit  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the unit is null; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Null units occur only when you create compound units in which all the units cancel out. For example, if you tried to create a unit by dividing deciliters by liters (`dL/L`), you would end up with a null unit.

## See Also

- [convenience init(from: String)](hkunit/init(from:)-9qont.md)
  Returns the unit instance described by the provided string.
- [var unitString: String](hkunit/unitstring.md)
  A string representation of the unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/isnull())*