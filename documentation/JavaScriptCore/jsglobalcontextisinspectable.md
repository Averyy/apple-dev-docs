# JSGlobalContextIsInspectable(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Returns a Boolean value that indicates whether the JavaScript context is inspectable.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextIsInspectable(_ ctx: JSGlobalContextRef!) -> Bool
```

#### Return Value

A Boolean value that indicates whether the JavaScript context is inspectable.

## Parameters

- `ctx`: The   to check whether it’s inspectable.

## Topics

### Related Documentation
- [func JSGlobalContextCopyName(JSGlobalContextRef!) -> JSStringRef!](jsglobalcontextcopyname(_:).md)
  Gets a copy of the name of a context.
- [func JSGlobalContextSetName(JSGlobalContextRef!, JSStringRef!)](jsglobalcontextsetname(_:_:).md)
  Sets the remote debugging name for a context.

## See Also

- [func JSGlobalContextSetInspectable(JSGlobalContextRef!, Bool)](jsglobalcontextsetinspectable(_:_:).md)
  Sets a JavaScript context to be either inspectable or not inspectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextisinspectable(_:))*