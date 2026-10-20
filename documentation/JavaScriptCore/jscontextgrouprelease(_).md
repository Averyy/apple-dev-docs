# JSContextGroupRelease(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Releases a JavaScript context group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGroupRelease(_ group: JSContextGroupRef!)
```

```c
void JSContextGroupRelease(JSContextGroupRef group);
```

## Parameters

- `group`: The [`JSContextGroupRef`](./jscontextgroupref.md) to release.

## See Also

### Creating a Context Group
- [func JSContextGroupCreate() -> JSContextGroupRef!](./jscontextgroupcreate%28%29.md)
  Creates a JavaScript context group.
- [func JSContextGroupRetain(JSContextGroupRef!) -> JSContextGroupRef!](./jscontextgroupretain%28_%29.md)
  Retains a JavaScript context group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgrouprelease(_:))*