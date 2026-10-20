# takeStringValueFrom(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the receiver’s cell to the string value obtained from the specified object.

**Availability**:
- macOS

## Declaration

```swift
func takeStringValueFrom(_ sender: Any?)
```

```objc
- (void) takeStringValueFrom:(id) sender;
```

## Parameters

- `sender`: The object from which to take the value. This object must implement the [`stringValue`](./stringvalue.md) property.

## See Also

### Related Documentation
- [var stringValue: String](./stringvalue.md)
  The cell’s value as a string.
### Deriving Values
- [func takeObjectValueFrom(Any?)](./takeobjectvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](./takeintegervaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntValueFrom(Any?)](./takeintvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeDoubleValueFrom(Any?)](./takedoublevaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](./takefloatvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/takestringvaluefrom(_:))*