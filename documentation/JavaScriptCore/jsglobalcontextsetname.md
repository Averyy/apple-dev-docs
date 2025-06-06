# JSGlobalContextSetName(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Sets the remote debugging name for a context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextSetName(_ ctx: JSGlobalContextRef!, _ name: JSStringRef!)
```

## Parameters

- `ctx`: The   that you want to name.
- `name`: The remote debugging name to set on  .

## See Also

- [func JSGlobalContextCopyName(JSGlobalContextRef!) -> JSStringRef!](jsglobalcontextcopyname(_:).md)
  Gets a copy of the name of a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextsetname(_:_:))*