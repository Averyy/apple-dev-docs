# toRect()

**Framework**: JavaScriptCore  
**Kind**: method

Converts the value to a rectangle structure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func toRect() -> CGRect
```

#### Return Value

A CoreGraphics point representation of the value.

#### Discussion

This method treats the value as a JavaScript object, reading the values of its `x`, `y`, `width`, and `height` properties using the [`toDouble()`](jsvalue/todouble().md) method and creating a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) structure from the result. If the value is not a JavaScript object or does not have the appropriate properties, each of the resulting rectangle’s coordinates is not a number (NaN).

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
- [func toDictionary() -> [AnyHashable : Any]!](jsvalue/todictionary.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](jsvalue/topoint.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](jsvalue/torange.md)
  Converts the value to a range.
- [func toSize() -> CGSize](jsvalue/tosize.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/torect())*