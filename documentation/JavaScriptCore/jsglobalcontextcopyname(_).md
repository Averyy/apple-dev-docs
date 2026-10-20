# JSGlobalContextCopyName(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Gets a copy of the name of a context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGlobalContextCopyName(_ ctx: JSGlobalContextRef!) -> JSStringRef!
```

```c
JSStringRefJSGlobalContextCopyName(JSGlobalContextRef ctx);
```

#### Return Value

The name for `ctx`.

#### Discussion

JavaScriptCore exposes the name of [`JSGlobalContextRef`](./jsglobalcontextref.md) for remote debugging to make it easier to identify the context you want to attach to.

## Parameters

- `ctx`: The [`JSGlobalContextRef`](./jsglobalcontextref.md) with the name you want to get.

## See Also

### Managing the context’s name
- [func JSGlobalContextSetName(JSGlobalContextRef!, JSStringRef!)](./jsglobalcontextsetname%28_,_%29.md)
  Sets the remote debugging name for a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextcopyname(_:))*