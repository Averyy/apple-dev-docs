# init(newPromiseRejectedWithReason:in:)

**Framework**: JavaScriptCore  
**Kind**: init  
**Role**: Initializer

Creates a rejected promise object with the specified value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(newPromiseRejectedWithReason reason: Any!, in context: JSContext!)
```

```objc
+ (JSValue *) valueWithNewPromiseRejectedWithReason:(id) reason inContext:(JSContext *) context;
```

## Return Value

A [`JSValue`](../jsvalue.md) that represents a new promise JavaScript object.

## Discussion

This method is equivalent to calling the following:

```objc
[JSValue valueWithNewPromiseFromExecutor:^(JSValue *resolve, JSValue *reject) { 
    [reject callWithArguments:@[reason]]; 
} inContext:context];
```

## Parameters

- `reason`: The result value to pass to any reactions.
- `context`: The [`JSContext`](../jscontext.md) the resulting [`JSValue`](../jsvalue.md) belongs to.

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
- [+ valueWithNewSymbolFromDescription:inContext:](./init%28newsymbolfromdescription,in%29.md)
  Creates a unique symbol object.
- [+ valueWithNewPromiseInContext:fromExecutor:](./init%28newpromisein,fromexecutor%29.md)
  Creates a promise object using the specified executor callback.
- [+ valueWithNewPromiseResolvedWithResult:inContext:](./init%28newpromiseresolvedwithresult,in%29.md)
  Creates a resolved promise object with the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newpromiserejectedwithreason:in:))*