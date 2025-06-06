# JSContextGroupRef

**Framework**: JavaScriptCore  
**Kind**: typealias

A group that associates JavaScript contexts with one another.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSContextGroupRef = OpaquePointer
```

#### Discussion

Contexts in the same group may share and exchange JavaScript objects.

## Topics

### Accessing the Content Group
- [func JSContextGetGroup(JSContextRef!) -> JSContextGroupRef!](jscontextgetgroup(_:).md)
  Gets the context group that a JavaScript execution context belongs to.

## See Also

- [typealias JSContextRef](jscontextref.md)
  A JavaScript execution context.
- [typealias JSGlobalContextRef](jsglobalcontextref.md)
  A global JavaScript execution context.
- [typealias JSStringRef](jsstringref.md)
  A UTF-16 character buffer.
- [typealias JSClassRef](jsclassref.md)
  A JavaScript class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgroupref)*