# init(newPromiseIn:fromExecutor:)

**Framework**: JavaScriptCore  
**Kind**: init  
**Role**: Initializer

Creates a promise object using the specified executor callback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(newPromiseIn context: JSContext!, fromExecutor callback: ((JSValue?, JSValue?) -> Void)!)
```

```objc
+ (JSValue *) valueWithNewPromiseInContext:(JSContext *) context fromExecutor:(void (^)(JSValue *resolve, JSValue *reject)) callback;
```

#### Return Value

A [`JSValue`](../jsvalue.md) that represents a new promise JavaScript object.

#### Discussion

This method is equivalent to calling the `Promise()` constructor in JavaScript.

The `resolve` and `reject` callbacks each typically take a single value, which they forward to all relevant pending reactions. While inside the executor callback, `context` acts as if it is in any other callback, except `calleeFunction` is `nil`. This also means you can access the new promise object using `[context thisValue]`.

## Parameters

- `context`: The [`JSContext`](../jscontext.md) the resulting [`JSValue`](../jsvalue.md) belongs to.
- `callback`: A callback block to invoke during initialization of the promise object. The `resolve` and `reject` parameters are functions that you can call to notify any pending reactions about the state of the new promise object.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newpromisein:fromexecutor:))*