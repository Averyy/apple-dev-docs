# toDictionary()

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Converts the JavaScript value to a dictionary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func toDictionary() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) toDictionary;
```

## Return Value

The dictionary representation of the value.

## Discussion

If the value is a JavaScript object, this method creates an [`NSDictionary`](../../Foundation/nsdictionary.md) object of the corresponding size, and recursively copies and converts all enumerable properties of the object into the dictionary with correspondingly named keys. JavaScript converts each element to a native object using the rules listed in [Convert Between JavaScript and Native Types](../jsvalue.md#Convert-Between-JavaScript-and-Native-Types).

This method returns `nil` if the JavaScript value is `null` or `undefined`, and throws a JavaScript `TypeError` if the value is not a JavaScript object.

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
- [func toPoint() -> CGPoint](./topoint%28%29.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](./torange%28%29.md)
  Converts the value to a range.
- [func toRect() -> CGRect](./torect%28%29.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](./tosize%28%29.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/todictionary())*