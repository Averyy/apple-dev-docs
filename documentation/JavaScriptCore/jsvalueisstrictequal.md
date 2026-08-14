# JSValueIsStrictEqual(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the two values are strict equal according to the JavaScript `===` operator; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `ctx`: The execution context to use.
- `a`: The first value to test.
- `b`: The second value to test.

## See Also

- [func JSValueIsEqual(JSContextRef!, JSValueRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsvalueisequal(_:_:_:_:).md)
  Tests whether two JavaScript values are equal.
- [func JSValueIsInstanceOfConstructor(JSContextRef!, JSValueRef!, JSObjectRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsvalueisinstanceofconstructor(_:_:_:_:).md)
  Tests whether a JavaScript value is an object that the specified constructor creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisstrictequal(_:_:_:))*