# JSClassRef

**Framework**: JavaScriptCore  
**Kind**: typealias

A JavaScript class.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSClassRef = OpaquePointer
```

#### Discussion

Use this type with [`JSObjectMake(_:_:_:)`](jsobjectmake(_:_:_:).md) to construct objects with custom behavior.

## See Also

- [typealias JSContextGroupRef](jscontextgroupref.md)
  A group that associates JavaScript contexts with one another.
- [typealias JSContextRef](jscontextref.md)
  A JavaScript execution context.
- [typealias JSGlobalContextRef](jsglobalcontextref.md)
  A global JavaScript execution context.
- [typealias JSStringRef](jsstringref.md)
  A UTF-16 character buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsclassref)*