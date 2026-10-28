# init(newRegularExpressionFromPattern:flags:in:)

**Framework**: JavaScriptCore  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (JSValue *) valueWithNewRegularExpressionFromPattern:(NSString *) pattern flags:(NSString *) flags inContext:(JSContext *) context;
```

## Return Value

A new JavaScript regular expression object.

## Discussion

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

### Creating JavaScript Values
- [init!(object: Any!, in: JSContext!)](./init%28object,in%29.md)
  Creates a JavaScript value by converting the specified native object.
- [init!(bool: Bool, in: JSContext!)](./init%28bool,in%29.md)
  Creates a JavaScript representation of the specified Boolean value.
- [init!(double: Double, in: JSContext!)](./init%28double,in%29.md)
  Creates a JavaScript representation of the specified floating-point value.
- [init!(int32: Int32, in: JSContext!)](./init%28int32,in%29.md)
  Creates a JavaScript representation of the specified signed integer value.
- [init!(uInt32: UInt32, in: JSContext!)](./init%28uint32,in%29.md)
  Creates a JavaScript representation of the specified unsigned integer value.
- [init!(newObjectIn: JSContext!)](./init%28newobjectin%29.md)
  Creates a new, empty JavaScript object value.
- [init!(newArrayIn: JSContext!)](./init%28newarrayin%29.md)
  Creates a new, empty JavaScript array value.
- [init!(newErrorFromMessage: String!, in: JSContext!)](./init%28newerrorfrommessage,in%29.md)
  Creates a JavaScript error value with the specified error message.
- [init!(undefinedIn: JSContext!)](./init%28undefinedin%29.md)
  Creates a JavaScript `undefined` value.
- [init!(nullIn: JSContext!)](./init%28nullin%29.md)
  Creates a JavaScript `null` value.
- [init!(point: CGPoint, inContext: JSContext!)](./init%28point,incontext%29.md)
  Creates a JavaScript representation of the specified point.
- [init!(range: NSRange, inContext: JSContext!)](./init%28range,incontext%29.md)
  Creates a JavaScript representation of the specified range.
- [init!(rect: CGRect, inContext: JSContext!)](./init%28rect,incontext%29.md)
  Creates a JavaScript representation of the specified rectangle.
- [init!(size: CGSize, inContext: JSContext!)](./init%28size,incontext%29.md)
  Creates a JavaScript representation of the specified width and height.
- [init!(newSymbolFromDescription: String!, in: JSContext!)](./init%28newsymbolfromdescription,in%29.md)
  Creates a unique symbol object.
- [+ valueWithNewPromiseInContext:fromExecutor:](./init%28newpromisein,fromexecutor%29.md)
  Creates a promise object using the specified executor callback.
- [+ valueWithNewPromiseRejectedWithReason:inContext:](./init%28newpromiserejectedwithreason,in%29.md)
  Creates a rejected promise object with the specified value.
- [+ valueWithNewPromiseResolvedWithResult:inContext:](./init%28newpromiseresolvedwithresult,in%29.md)
  Creates a resolved promise object with the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newregularexpressionfrompattern:flags:in:))*