# JSContextGroupRetain(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Retains a JavaScript context group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGroupRetain(_ group: JSContextGroupRef!) -> JSContextGroupRef!
```

#### Return Value

A [`JSContextGroupRef`](jscontextgroupref.md) that is the same as `group`.

## Parameters

- `group`: The   to retain.

## See Also

- [func JSContextGroupCreate() -> JSContextGroupRef!](jscontextgroupcreate().md)
  Creates a JavaScript context group.
- [func JSContextGroupRelease(JSContextGroupRef!)](jscontextgrouprelease(_:).md)
  Releases a JavaScript context group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgroupretain(_:))*