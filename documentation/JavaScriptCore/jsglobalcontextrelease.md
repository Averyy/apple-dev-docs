# JSGlobalContextRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Releases a global JavaScript execution context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextRelease(_ ctx: JSGlobalContextRef!)
```

## Parameters

- `ctx`: The   to release.

## See Also

- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreate(_:).md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextCreateInGroup(JSContextGroupRef!, JSClassRef!) -> JSGlobalContextRef!](jsglobalcontextcreateingroup(_:_:).md)
  Creates a global JavaScript execution context in the provided context group.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](jsglobalcontextretain(_:).md)
  Retains a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextrelease(_:))*