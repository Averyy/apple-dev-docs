# takeDoubleValueFrom(_:)

**Framework**: AppKit  
**Kind**: method

Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func takeDoubleValueFrom(_ sender: Any?)
```

## Parameters

- `sender`: The object from which to take the value. This object must implement the   property.

## See Also

- [var doubleValue: Double](nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [func takeObjectValueFrom(Any?)](nscell/takeobjectvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](nscell/takeintegervaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntValueFrom(Any?)](nscell/takeintvaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeStringValueFrom(Any?)](nscell/takestringvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](nscell/takefloatvaluefrom(_:).md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/takedoublevaluefrom(_:))*