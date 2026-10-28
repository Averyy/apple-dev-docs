# takeIntValueFrom(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the receiver’s cell to an integer value obtained from the specified object.

**Availability**:
- macOS

## Declaration

```swift
func takeIntValueFrom(_ sender: Any?)
```

```objc
- (void) takeIntValueFrom:(id) sender;
```

## Discussion

Use the [`takeIntegerValueFrom(_:)`](./takeintegervaluefrom%28_%29.md) method instead.

## Parameters

- `sender`: The object from which to take the value. This object must implement the [`intValue`](./intvalue.md) property.

## See Also

### Related Documentation
- [var integerValue: Int](./integervalue.md)
  The cell’s value as an integer value.
### Deriving Values
- [func takeObjectValueFrom(Any?)](./takeobjectvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](./takeintegervaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeStringValueFrom(Any?)](./takestringvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
- [func takeDoubleValueFrom(Any?)](./takedoublevaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](./takefloatvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/takeintvaluefrom(_:))*