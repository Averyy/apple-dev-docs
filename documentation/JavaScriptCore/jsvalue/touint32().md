# toUInt32()

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Converts the JavaScript value to a native unsigned integer value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func toUInt32() -> UInt32
```

```objc
- (uint32_t) toUInt32;
```

#### Return Value

The native unsigned 32-bit integer value.

#### Discussion

This method uses JavaScript type coercion to convert the value to a JavaScript integer value, then returns a native representation of the result. In JavaScript, all numeric values are treated as double-precision floating-point numbers except for certain operations such as bit shifts.

## See Also

### Reading and Converting JavaScript Values
- [func toObject() -> Any!](./toobject%28%29.md)
  Converts the JavaScript value to a native object.
- [func toObjectOf(AnyClass!) -> Any!](./toobjectof%28_%29.md)
  Converts the JavaScript value to a native object of the specified class.
- [func toBool() -> Bool](./tobool%28%29.md)
  Converts the JavaScript value to a native Boolean value.
- [func toDouble() -> Double](./todouble%28%29.md)
  Converts the JavaScript value to a native floating-point value.
- [func toInt32() -> Int32](./toint32%28%29.md)
  Converts the JavaScript value to a native signed integer value.
- [func toNumber() -> NSNumber!](./tonumber%28%29.md)
  Converts the JavaScript value to a [`NSNumber`](../../Foundation/nsnumber.md) object.
- [func toString() -> String!](./tostring%28%29.md)
  Converts the JavaScript value to a native string.
- [func toDate() -> Date!](./todate%28%29.md)
  Converts the JavaScript value to a date object.
- [func toArray() -> [Any]!](./toarray%28%29.md)
  Converts the JavaScript value to an array.
- [func toDictionary() -> [AnyHashable : Any]!](./todictionary%28%29.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](./topoint%28%29.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](./torange%28%29.md)
  Converts the value to a range.
- [func toRect() -> CGRect](./torect%28%29.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](./tosize%28%29.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/touint32())*