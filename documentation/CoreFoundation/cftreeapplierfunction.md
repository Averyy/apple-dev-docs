# CFTreeApplierFunction

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Type of the callback function used by the CFTree apply function.

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
typealias CFTreeApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(const void *, void *) CFTreeApplierFunction;
```

#### Discussion

This callback is used by the [`CFTreeApplyFunctionToChildren(_:_:_:)`](./cftreeapplyfunctiontochildren%28_,_,_%29.md) applier function.

## Parameters

- `value`: The current child of a tree that is being iterated.
- `context`: The program-defined context parameter that was passed to the applier function.

## See Also

### Callbacks
- [typealias CFTreeCopyDescriptionCallBack](./cftreecopydescriptioncallback.md)
  Callback function used to provide a description of the program-defined information pointer.
- [typealias CFTreeReleaseCallBack](./cftreereleasecallback.md)
  Callback function used to release a previously retained program-defined information pointer.
- [typealias CFTreeRetainCallBack](./cftreeretaincallback.md)
  Callback function used to retain a program-defined information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeapplierfunction)*