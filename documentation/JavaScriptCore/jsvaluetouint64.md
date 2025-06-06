# JSValueToUInt64(_:_:_:)

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
func JSValueToUInt64(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> UInt64
```

#### Discussion

```None
@function
@abstract         Converts a JSValue to an unsigned 64-bit integer and returns the resulting integer.
@param ctx        The execution context to use.
@param value      The JSValue to convert.
@param exception  A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.
@result           A uint64_t with the result of conversion, or 0 if an exception is thrown. Since 0 is valid value, `exception` must be checked after the call.
@discussion       The JSValue is converted to an integer according to the rules specified by the JavaScript language. If the value is a BigInt, then the JSValue is truncated to a uint64_t.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluetouint64(_:_:_:))*