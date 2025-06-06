# JSValueCreateJSONString(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript string that contains the JSON-serialized representation of a JavaScript value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueCreateJSONString(_ ctx: JSContextRef!, _ value: JSValueRef!, _ indent: UInt32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!
```

#### Return Value

A [`JSStringRef`](jsstringref.md) with the result of serialization, or `NULL` if the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `value`: The value to serialize.
- `indent`: The number of spaces to indent when nesting. If  , the resulting JSON string doesn’t contain new lines. The size of the indent clamps to 10 spaces.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSValueMakeFromJSONString(JSContextRef!, JSStringRef!) -> JSValueRef!](jsvaluemakefromjsonstring(_:_:).md)
  Creates a JavaScript value from a JSON-formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluecreatejsonstring(_:_:_:_:))*