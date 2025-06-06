# init(newRegularExpressionFromPattern:flags:in:)

**Framework**: JavaScriptCore  
**Kind**: init

Creates a JavaScript regular expression value from the specified pattern.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(newRegularExpressionFromPattern pattern: String!, flags: String!, in context: JSContext!)
```

#### Return Value

A new JavaScript regular expression object.

#### Discussion

Calling this method creates a JavaScript `RegExp` object, and is equivalent to declaring a regular expression literal (such as `/ab+c/i`) or calling the `RegExp` constructor (for example, `new RegExp("ab+c", "i")`) in JavaScript.

The `flags` parameter can include any of the following options:

- `g` (global match): match all occurrences of the pattern in a string, not just the first.
- `i` (ignore case): perform case-insensitive search.
- `m` (multiline): treat the `^` and `$` regular expression tokens as matching the start or end of any line in a string (as delimited by newline or return characters), not just the start or end of the entire string.

## Parameters

- `pattern`: A string to be interpreted as a regular expression pattern.
- `flags`: A combination of zero or more single-letter flags specifying search options.
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
- [init!(newObjectIn: JSContext!)](jsvalue/init(newobjectin:).md)
  Creates a new, empty JavaScript object value.
- [init!(newArrayIn: JSContext!)](jsvalue/init(newarrayin:).md)
  Creates a new, empty JavaScript array value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newregularexpressionfrompattern:flags:in:))*