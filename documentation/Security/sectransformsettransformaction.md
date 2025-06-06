# SecTransformSetTransformAction(_:_:_:)

**Framework**: Security  
**Kind**: func

Changes the way that a transform deals with transform lifecycle behaviors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: @escaping SecTransformActionBlock) -> CFError?
```

#### Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the error’s memory when you are done with it.

## Parameters

- `ref`: A custom transform.
- `action`: The behavior to change. Valid values are  ,  ,  , or  .
- `newAction`: A   block that implements the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformsettransformaction(_:_:_:))*