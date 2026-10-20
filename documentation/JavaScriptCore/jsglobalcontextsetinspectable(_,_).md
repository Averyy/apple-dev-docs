# JSGlobalContextSetInspectable(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

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

```c
void JSGlobalContextSetInspectable(JSGlobalContextRef ctx, bool inspectable);
```

## Parameters

- `ctx`: The [`JSGlobalContextRef`](./jsglobalcontextref.md) to set whether it’s inspectable.
- `inspectable`: A Boolean value that indicates whether the context is inspectable.

## Topics

### Related Documentation
- [func JSGlobalContextCopyName(JSGlobalContextRef!) -> JSStringRef!](./jsglobalcontextcopyname%28_%29.md)
  Gets a copy of the name of a context.
- [func JSGlobalContextSetName(JSGlobalContextRef!, JSStringRef!)](./jsglobalcontextsetname%28_,_%29.md)
  Sets the remote debugging name for a context.

## See Also

### Making a context inspectable
- [func JSGlobalContextIsInspectable(JSGlobalContextRef!) -> Bool](./jsglobalcontextisinspectable%28_%29.md)
  Returns a Boolean value that indicates whether the JavaScript context is inspectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextsetinspectable(_:_:))*