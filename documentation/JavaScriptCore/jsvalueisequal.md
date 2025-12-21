# JSValueIsEqual(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Tests whether two JavaScript values are equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueIsEqual(_ ctx: JSContextRef!, _ a: JSValueRef!, _ b: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the two values are equal according to the JavaScript `==` operator; [`false`](https://developer.apple.com/documentation/Swift/false) if they’re unequal or the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `a`: The first value to test.
- `b`: The second value to test.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSValueIsStrictEqual(JSContextRef!, JSValueRef!, JSValueRef!) -> Bool](jsvalueisstrictequal(_:_:_:).md)
  Tests whether two JavaScript values are strict equal.
- [func JSValueIsInstanceOfConstructor(JSContextRef!, JSValueRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsvalueisinstanceofconstructor(_:_:_:_:).md)
  Tests whether a JavaScript value is an object that the specified constructor creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisequal(_:_:_:_:))*