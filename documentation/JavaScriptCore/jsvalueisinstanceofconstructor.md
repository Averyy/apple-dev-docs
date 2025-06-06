# JSValueIsInstanceOfConstructor(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value is an object that `constructor` creates, according to the JavaScript `instanceof` operator; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `ctx`: The execution context to use.
- `value`: The   to test.
- `constructor`: The constructor to test against.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSValueIsEqual(JSContextRef!, JSValueRef!, JSValueRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsvalueisequal(_:_:_:_:).md)
  Tests whether two JavaScript values are equal.
- [func JSValueIsStrictEqual(JSContextRef!, JSValueRef!, JSValueRef!) -> Bool](jsvalueisstrictequal(_:_:_:).md)
  Tests whether two JavaScript values are strict equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisinstanceofconstructor(_:_:_:_:))*