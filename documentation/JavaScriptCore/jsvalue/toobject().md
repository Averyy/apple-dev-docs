# toObject()

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Converts the JavaScript value to a native object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func toObject() -> Any!
```

```objc
- (id) toObject;
```

## Return Value

An Objective-C or Swift object representing the JavaScript value.

## Discussion

The type of the resulting object depends on the contents of the JavaScript value. For conversion rules, see [Convert Between JavaScript and Native Types](../jsvalue.md#Convert-Between-JavaScript-and-Native-Types).

## See Also

### Reading and Converting JavaScript Values
- [func toObjectOf(AnyClass!) -> Any!](./toobjectof%28_%29.md)
  Converts the JavaScript value to a native object of the specified class.
- [func toBool() -> Bool](./tobool%28%29.md)
  Converts the JavaScript value to a native Boolean value.
- [func toDouble() -> Double](./todouble%28%29.md)
  Converts the JavaScript value to a native floating-point value.
- [func toInt32() -> Int32](./toint32%28%29.md)
  Converts the JavaScript value to a native signed integer value.
- [func toUInt32() -> UInt32](./touint32%28%29.md)
  Converts the JavaScript value to a native unsigned integer value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/toobject())*