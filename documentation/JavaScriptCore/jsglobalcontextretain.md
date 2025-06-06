# JSGlobalContextRetain(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Retains a global JavaScript execution context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextRetain(_ ctx: JSGlobalContextRef!) -> JSGlobalContextRef!
```

#### Return Value

A [`JSGlobalContextRef`](jsglobalcontextref.md) that is the same as `ctx`.

## Parameters

- `ctx`: The   to retain.

## See Also

- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreate(_:).md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextCreateInGroup(JSContextGroupRef!, JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreateingroup(_:_:).md)
  Creates a global JavaScript execution context in the provided context group.
- [func JSGlobalContextRelease(JSGlobalContextRef!)](jsglobalcontextrelease(_:).md)
  Releases a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextretain(_:))*