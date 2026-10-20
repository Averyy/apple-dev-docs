# JSGlobalContextRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

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

```c
void JSGlobalContextRelease(JSGlobalContextRef ctx);
```

## Parameters

- `ctx`: The [`JSGlobalContextRef`](./jsglobalcontextref.md) to release.

## See Also

### Creating a global context
- [func JSGlobalContextCreate(JSClassRef!) -> JSGlobalContextRef!](./jsglobalcontextcreate%28_%29.md)
  Creates a global JavaScript execution context.
- [func JSGlobalContextCreateInGroup(JSContextGroupRef!, JSClassRef!) -> JSGlobalContextRef!](./jsglobalcontextcreateingroup%28_,_%29.md)
  Creates a global JavaScript execution context in the provided context group.
- [func JSGlobalContextRetain(JSGlobalContextRef!) -> JSGlobalContextRef!](./jsglobalcontextretain%28_%29.md)
  Retains a global JavaScript execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextrelease(_:))*