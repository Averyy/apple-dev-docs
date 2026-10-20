# JSContextRef

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

A JavaScript execution context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSContextRef = OpaquePointer
```

```c
typedef const struct OpaqueJSContext * JSContextRef;
```

#### Discussion

This holds the global object and other execution state.

## Topics

### Creating a Context Group
- [func JSContextGroupCreate() -> JSContextGroupRef!](./jscontextgroupcreate%28%29.md)
  Creates a JavaScript context group.
- [func JSContextGroupRetain(JSContextGroupRef!) -> JSContextGroupRef!](./jscontextgroupretain%28_%29.md)
  Retains a JavaScript context group.
- [func JSContextGroupRelease(JSContextGroupRef!)](./jscontextgrouprelease%28_%29.md)
  Releases a JavaScript context group.
### Accessing the Global Context
- [func JSContextGetGlobalContext(JSContextRef!) -> JSGlobalContextRef!](./jscontextgetglobalcontext%28_%29.md)
  Gets the global context of a JavaScript execution context.

## See Also

### JavaScriptCore Engine Interface
- [typealias JSContextGroupRef](./jscontextgroupref.md)
  A group that associates JavaScript contexts with one another.
- [typealias JSGlobalContextRef](./jsglobalcontextref.md)
  A global JavaScript execution context.
- [typealias JSStringRef](./jsstringref.md)
  A UTF-16 character buffer.
- [typealias JSClassRef](./jsclassref.md)
  A JavaScript class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextref)*