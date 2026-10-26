# init(newErrorFromMessage:in:)

**Framework**: JavaScriptCore  
**Kind**: init  
**Role**: Initializer

Creates a JavaScript error value with the specified error message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(newErrorFromMessage message: String!, in context: JSContext!)
```

```objc
+ (JSValue *) valueWithNewErrorFromMessage:(NSString *) message inContext:(JSContext *) context;
```

#### Return Value

A new JavaScript error value.

#### Discussion

Calling this method creates a JavaScript `Error` object, and is equivalent to calling the `Error` constructor (for example, `new Error("message")`) in JavaScript.

## Parameters

- `message`: The error message for the error object.
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
- [init!(newRegularExpressionFromPattern: String!, flags: String!, in: JSContext!)](./init%28newregularexpressionfrompattern,flags,in%29.md)
  Creates a JavaScript regular expression value from the specified pattern.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newerrorfrommessage:in:))*