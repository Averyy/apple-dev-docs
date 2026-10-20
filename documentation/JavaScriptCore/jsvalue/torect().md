# toRect()

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGRect) toRect;
```

#### Return Value

A CoreGraphics point representation of the value.

#### Discussion

This method treats the value as a JavaScript object, reading the values of its `x`, `y`, `width`, and `height` properties using the [`toDouble()`](./todouble%28%29.md) method and creating a [`CGRect`](../../CoreFoundation/cgrect.md) structure from the result. If the value is not a JavaScript object or does not have the appropriate properties, each of the resulting rectangle’s coordinates is not a number (NaN).

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
- [func toDictionary() -> [AnyHashable : Any]!](./todictionary%28%29.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](./topoint%28%29.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](./torange%28%29.md)
  Converts the value to a range.
- [func toSize() -> CGSize](./tosize%28%29.md)
  Converts the value to a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/torect())*