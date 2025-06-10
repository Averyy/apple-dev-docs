# JSBigIntCreateWithString(_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 9.0+
- visionOS 2.0+

## Declaration

```swift
func JSBigIntCreateWithString(_ ctx: JSContextRef, _ string: JSStringRef, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef
```

#### Return Value

A BigInt JSValue of the string, or NULL if an exception is thrown.

#### Discussion

This is equivalent to calling the `BigInt` constructor from JavaScript with a string argument.

## Parameters

- `ctx`: The execution context to use.
- `string`: The JSStringRef representation of an integer.
- `exception`: A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithstring(_:_:_:))*