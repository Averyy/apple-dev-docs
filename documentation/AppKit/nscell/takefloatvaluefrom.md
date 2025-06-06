# takeFloatValueFrom(_:)

**Framework**: AppKit  
**Kind**: method

Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func takeFloatValueFrom(_ sender: Any?)
```

## Parameters

- `sender`: The object from which to take the value. This object must implement the   property.

## See Also

- [var floatValue: Float](nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.
- [func takeObjectValueFrom(Any?)](nscell/takeobjectvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](nscell/takeintegervaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntValueFrom(Any?)](nscell/takeintvaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeStringValueFrom(Any?)](nscell/takestringvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
- [func takeDoubleValueFrom(Any?)](nscell/takedoublevaluefrom(_:).md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/takefloatvaluefrom(_:))*