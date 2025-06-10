# JSBigIntCreateWithDouble(_:_:_:)

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
func JSBigIntCreateWithDouble(_ ctx: JSContextRef, _ value: Double, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef
```

#### Return Value

A BigInt JSValue of the value, or NULL if an exception is thrown.

#### Discussion

If the value is not an integer, an exception is thrown.

## Parameters

- `ctx`: The execution context to use.
- `value`: The value to copy into the new BigInt JSValue.
- `exception`: A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithdouble(_:_:_:))*