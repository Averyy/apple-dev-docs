# init(JSGlobalContextRef:)

**Framework**: JavaScriptCore  
**Kind**: init

Creates a JavaScript context object from the equivalent C representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(jsGlobalContextRef: JSGlobalContextRef!)
```

#### Return Value

A JavaScript context object representing the same context.

#### Discussion

See `JSContextRef` for the C JavaScriptCore API.

## Parameters

- `jsGlobalContextRef`: A C JavaScript context reference.

## See Also

- [var jsGlobalContextRef: JSGlobalContextRef!](jscontext/jsglobalcontextref.md)
  Returns the C representation of the JavaScript context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/init(jsglobalcontextref:))*