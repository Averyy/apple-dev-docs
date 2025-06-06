# init(JSValueRef:inContext:)

**Framework**: JavaScriptCore  
**Kind**: init

Creates a JavaScript value object from the equivalent C representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(jsValueRef value: JSValueRef!, in context: JSContext!)
```

#### Return Value

A JavaScript value object representing the same value.

#### Discussion

See `JSValueRef` for the C JavaScriptCore API.

## Parameters

- `value`: A C JavaScript value reference.
- `context`: The JavaScript context in which to create the value.

## See Also

- [var jsValueRef: JSValueRef!](jsvalue/jsvalueref.md)
  Returns the C representation of the JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(jsvalueref:incontext:))*