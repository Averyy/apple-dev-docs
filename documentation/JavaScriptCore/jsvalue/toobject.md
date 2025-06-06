# toObject()

**Framework**: JavaScriptCore  
**Kind**: method

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

#### Return Value

An Objective-C or Swift object representing the JavaScript value.

#### Discussion

The type of the resulting object depends on the contents of the JavaScript value. For conversion rules, see [`Convert Between JavaScript and Native Types`](jsvalue#Convert-Between-JavaScript-and-Native-Types.md).

## See Also

- [func toObjectOf(AnyClass!) -> Any!](jsvalue/toobjectof(_:).md)
  Converts the JavaScript value to a native object of the specified class.
- [func toBool() -> Bool](jsvalue/tobool.md)
  Converts the JavaScript value to a native Boolean value.
- [func toDouble() -> Double](jsvalue/todouble.md)
  Converts the JavaScript value to a native floating-point value.
- [func toInt32() -> Int32](jsvalue/toint32.md)
  Converts the JavaScript value to a native signed integer value.
- [func toUInt32() -> UInt32](jsvalue/touint32.md)
  Converts the JavaScript value to a native unsigned integer value.
- [func toNumber() -> NSNumber!](jsvalue/tonumber.md)
  Converts the JavaScript value to a [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object.
- [func toString() -> String!](jsvalue/tostring.md)
  Converts the JavaScript value to a native string.
- [func toDate() -> Date!](jsvalue/todate.md)
  Converts the JavaScript value to a date object.
- [func toArray() -> [Any]!](jsvalue/toarray.md)
  Converts the JavaScript value to an array.
- [func toDictionary() -> [AnyHashable : Any]!](jsvalue/todictionary.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](jsvalue/topoint.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](jsvalue/torange.md)
  Converts the value to a range.
- [func toRect() -> CGRect](jsvalue/torect.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](jsvalue/tosize.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/toobject())*