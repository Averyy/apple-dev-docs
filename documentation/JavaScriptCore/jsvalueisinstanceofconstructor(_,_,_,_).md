# JSValueIsInstanceOfConstructor(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Tests whether a JavaScript value is an object that the specified constructor creates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueIsInstanceOfConstructor(_ ctx: JSContextRef!, _ value: JSValueRef!, _ constructor: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool
```

```c
bool JSValueIsInstanceOfConstructor(JSContextRef ctx, JSValueRef value, JSObjectRef constructor, JSValueRef*exception);
```

#### Return Value

[`true`](../Swift/true.md) if the value is an object that `constructor` creates, according to the JavaScript `instanceof` operator; otherwise, [`false`](../Swift/false.md).

## Parameters

- `ctx`: The execution context to use.
- `value`: The [`JSValueRef`](./jsvalueref.md) to test.
- `constructor`: The constructor to test against.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store an exception in, if any. Pass `NULL` to discard any exception.

## See Also

### Comparing Values
- [func JSValueIsEqual(JSContextRef!, JSValueRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsvalueisequal%28_,_,_,_%29.md)
  Tests whether two JavaScript values are equal.
- [func JSValueIsStrictEqual(JSContextRef!, JSValueRef!, JSValueRef!) -> Bool](./jsvalueisstrictequal%28_,_,_%29.md)
  Tests whether two JavaScript values are strict equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisinstanceofconstructor(_:_:_:_:))*