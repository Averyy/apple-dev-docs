# init(newObjectIn:)

**Framework**: JavaScriptCore  
**Kind**: init

Creates a new, empty JavaScript object value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(newObjectIn context: JSContext!)
```

#### Return Value

An empty JavaScript object value.

#### Discussion

Calling this method is equivalent to declaring an empty object literal `{}` or using the `new Object()` syntax in JavaScript.

## Parameters

- `context`: The JavaScript context in which to create the value.

## See Also

- [init!(object: Any!, in: JSContext!)](jsvalue/init(object:in:).md)
  Creates a JavaScript value by converting the specified native object.
- [init!(bool: Bool, in: JSContext!)](jsvalue/init(bool:in:).md)
  Creates a JavaScript representation of the specified Boolean value.
- [init!(double: Double, in: JSContext!)](jsvalue/init(double:in:).md)
  Creates a JavaScript representation of the specified floating-point value.
- [init!(int32: Int32, in: JSContext!)](jsvalue/init(int32:in:).md)
  Creates a JavaScript representation of the specified signed integer value.
- [init!(uInt32: UInt32, in: JSContext!)](jsvalue/init(uint32:in:).md)
  Creates a JavaScript representation of the specified unsigned integer value.
- [init!(newArrayIn: JSContext!)](jsvalue/init(newarrayin:).md)
  Creates a new, empty JavaScript array value.
- [init!(newRegularExpressionFromPattern: String!, flags: String!, in: JSContext!)](jsvalue/init(newregularexpressionfrompattern:flags:in:).md)
  Creates a JavaScript regular expression value from the specified pattern.
- [init!(newErrorFromMessage: String!, in: JSContext!)](jsvalue/init(newerrorfrommessage:in:).md)
  Creates a JavaScript error value with the specified error message.
- [init!(undefinedIn: JSContext!)](jsvalue/init(undefinedin:).md)
  Creates a JavaScript `undefined` value.
- [init!(nullIn: JSContext!)](jsvalue/init(nullin:).md)
  Creates a JavaScript `null` value.
- [init!(point: CGPoint, inContext: JSContext!)](jsvalue/init(point:incontext:).md)
  Creates a JavaScript representation of the specified point.
- [init!(range: NSRange, inContext: JSContext!)](jsvalue/init(range:incontext:).md)
  Creates a JavaScript representation of the specified range.
- [init!(rect: CGRect, inContext: JSContext!)](jsvalue/init(rect:incontext:).md)
  Creates a JavaScript representation of the specified rectangle.
- [init!(size: CGSize, inContext: JSContext!)](jsvalue/init(size:incontext:).md)
  Creates a JavaScript representation of the specified width and height.
- [init!(newSymbolFromDescription: String!, in: JSContext!)](jsvalue/init(newsymbolfromdescription:in:).md)
  Creates a unique symbol object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newobjectin:))*