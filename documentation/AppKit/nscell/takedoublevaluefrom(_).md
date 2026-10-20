# takeDoubleValueFrom(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.

**Availability**:
- macOS

## Declaration

```swift
func takeDoubleValueFrom(_ sender: Any?)
```

```objc
- (void) takeDoubleValueFrom:(id) sender;
```

## Parameters

- `sender`: The object from which to take the value. This object must implement the [`doubleValue`](./doublevalue.md) property.

## See Also

### Related Documentation
- [var doubleValue: Double](./doublevalue.md)
  The cell’s value as a double-precision floating-point number.
### Deriving Values
- [func takeObjectValueFrom(Any?)](./takeobjectvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](./takeintegervaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntValueFrom(Any?)](./takeintvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeStringValueFrom(Any?)](./takestringvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](./takefloatvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/takedoublevaluefrom(_:))*