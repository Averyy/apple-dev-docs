# JSValueMakeFromJSONString(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a JavaScript value from a JSON-formatted string.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSValueMakeFromJSONString(_ ctx: JSContextRef!, _ string: JSStringRef!) -> JSValueRef!
```

#### Return Value

A [`JSValueRef`](jsvalueref.md) that contains the parsed value, or `NULL` if the input is invalid.

## Parameters

- `ctx`: The execution context to use.
- `string`: The   that contains the JSON string to parse.

## See Also

- [func JSValueCreateJSONString(JSContextRef!, JSValueRef!, UInt32, UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](jsvaluecreatejsonstring(_:_:_:_:).md)
  Creates a JavaScript string that contains the JSON-serialized representation of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluemakefromjsonstring(_:_:))*