# CFTreeRetainCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback function used to retain a program-defined information pointer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFTreeRetainCallBack = (UnsafeRawPointer?) -> UnsafeRawPointer?
```

```c
typedef const void *(*)(const void *) CFTreeRetainCallBack;
```

#### Return Value

The value to use whenever the information pointer is retained, which is usually the `info` parameter passed to this callback, but may be a different value if a different value should be used.

## Parameters

- `info`: The program-supplied information pointer provided in a [`CFTreeContext`](./cftreecontext.md) structure.

## See Also

### Callbacks
- [typealias CFTreeApplierFunction](./cftreeapplierfunction.md)
  Type of the callback function used by the CFTree apply function.
- [typealias CFTreeCopyDescriptionCallBack](./cftreecopydescriptioncallback.md)
  Callback function used to provide a description of the program-defined information pointer.
- [typealias CFTreeReleaseCallBack](./cftreereleasecallback.md)
  Callback function used to release a previously retained program-defined information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeretaincallback)*