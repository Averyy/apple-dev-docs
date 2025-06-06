# toDictionary()

**Framework**: JavaScriptCore  
**Kind**: method

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

#### Return Value

The dictionary representation of the value.

#### Discussion

If the value is a JavaScript object, this method creates an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object of the corresponding size, and recursively copies and converts all enumerable properties of the object into the dictionary with correspondingly named keys. JavaScript converts each element to a native object using the rules listed in [`Convert Between JavaScript and Native Types`](jsvalue#Convert-Between-JavaScript-and-Native-Types.md).

This method returns `nil` if the JavaScript value is `null` or `undefined`, and throws a JavaScript `TypeError` if the value is not a JavaScript object.

## See Also

- [func toObject() -> Any!](jsvalue/toobject.md)
  Converts the JavaScript value to a native object.
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
- [func toPoint() -> CGPoint](jsvalue/topoint.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](jsvalue/torange.md)
  Converts the value to a range.
- [func toRect() -> CGRect](jsvalue/torect.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](jsvalue/tosize.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/todictionary())*