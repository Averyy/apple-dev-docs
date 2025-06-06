# CFTreeReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback function used to release a previously retained program-defined information pointer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFTreeReleaseCallBack = (UnsafeRawPointer?) -> Void
```

## Parameters

- `info`: The program-supplied information pointer provided in a   structure.

## See Also

- [typealias CFTreeApplierFunction](cftreeapplierfunction.md)
  Type of the callback function used by the CFTree apply function.
- [typealias CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md)
  Callback function used to provide a description of the program-defined information pointer.
- [typealias CFTreeRetainCallBack](cftreeretaincallback.md)
  Callback function used to retain a program-defined information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreereleasecallback)*