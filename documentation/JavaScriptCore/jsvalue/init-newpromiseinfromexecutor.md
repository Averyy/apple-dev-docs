# init(newPromiseIn:fromExecutor:)

**Framework**: JavaScriptCore  
**Kind**: init

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

#### Return Value

A [`JSValue`](jsvalue.md) that represents a new promise JavaScript object.

#### Discussion

This method is equivalent to calling the `Promise()` constructor in JavaScript.

The `resolve` and `reject` callbacks each typically take a single value, which they forward to all relevant pending reactions. While inside the executor callback, `context` acts as if it is in any other callback, except `calleeFunction` is `nil`. This also means you can access the new promise object using `[context thisValue]`.

## Parameters

- `context`: The   the resulting   belongs to.
- `callback`: A callback block to invoke during initialization of the promise object. The   and   parameters are functions that you can call to notify any pending reactions about the state of the new promise object.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newpromisein:fromexecutor:))*