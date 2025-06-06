# JSGlobalContextSetInspectable(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Sets a JavaScript context to be either inspectable or not inspectable.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextSetInspectable(_ ctx: JSGlobalContextRef!, _ inspectable: Bool)
```

## Parameters

- `ctx`: The   to set whether it’s inspectable.
- `inspectable`: A Boolean value that indicates whether the context is inspectable.

## Topics

### Related Documentation
- [func JSGlobalContextCopyName(JSGlobalContextRef!) -> JSStringRef!](jsglobalcontextcopyname(_:).md)
  Gets a copy of the name of a context.
- [func JSGlobalContextSetName(JSGlobalContextRef!, JSStringRef!)](jsglobalcontextsetname(_:_:).md)
  Sets the remote debugging name for a context.

## See Also

- [func JSGlobalContextIsInspectable(JSGlobalContextRef!) -> Bool](jsglobalcontextisinspectable(_:).md)
  Returns a Boolean value that indicates whether the JavaScript context is inspectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextsetinspectable(_:_:))*