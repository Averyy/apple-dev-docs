# JSValueIsStrictEqual(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Tests whether two JavaScript values are strict equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueIsStrictEqual(_ ctx: JSContextRef!, _ a: JSValueRef!, _ b: JSValueRef!) -> Bool
```

```c
bool JSValueIsStrictEqual(JSContextRef ctx, JSValueRef a, JSValueRef b);
```

## Return Value

[`true`](../Swift/true.md) if the two values are strict equal according to the JavaScript `===` operator; otherwise, [`false`](../Swift/false.md).

## Parameters

- `ctx`: The execution context to use.
- `a`: The first value to test.
- `b`: The second value to test.

## See Also

### Comparing Values
- [func JSValueIsEqual(JSContextRef!, JSValueRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsvalueisequal%28_,_,_,_%29.md)
  Tests whether two JavaScript values are equal.
- [func JSValueIsInstanceOfConstructor(JSContextRef!, JSValueRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jsvalueisinstanceofconstructor%28_,_,_,_%29.md)
  Tests whether a JavaScript value is an object that the specified constructor creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisstrictequal(_:_:_:))*