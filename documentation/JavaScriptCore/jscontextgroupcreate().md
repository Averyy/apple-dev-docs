# JSContextGroupCreate()

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Creates a JavaScript context group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGroupCreate() -> JSContextGroupRef!
```

```c
JSContextGroupRefJSContextGroupCreate();
```

#### Return Value

The created [`JSContextGroupRef`](./jscontextgroupref.md).

#### Discussion

A [`JSContextGroupRef`](./jscontextgroupref.md) associates JavaScript contexts with one another. Contexts in the same group may share and exchange JavaScript objects. Sharing and exchanging JavaScript objects between contexts in different groups produces undefined behavior. When you use objects from the same context group in multiple threads, explicit synchronization is a requirement.

## See Also

### Creating a Context Group
- [func JSContextGroupRetain(JSContextGroupRef!) -> JSContextGroupRef!](./jscontextgroupretain%28_%29.md)
  Retains a JavaScript context group.
- [func JSContextGroupRelease(JSContextGroupRef!)](./jscontextgrouprelease%28_%29.md)
  Releases a JavaScript context group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgroupcreate())*