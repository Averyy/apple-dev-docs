# JSBigIntCreateWithUInt64(_:_:_:)

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
func JSBigIntCreateWithUInt64(_ ctx: JSContextRef, _ integer: UInt64, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef
```

#### Return Value

A BigInt JSValue of the integer, or NULL if an exception is thrown.

## Parameters

- `ctx`: The execution context to use.
- `integer`: The 64-bit unsigned integer to copy into the new BigInt JSValue.
- `exception`: A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithuint64(_:_:_:))*