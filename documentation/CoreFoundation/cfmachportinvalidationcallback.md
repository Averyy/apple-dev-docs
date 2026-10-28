# CFMachPortInvalidationCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback invoked when a CFMachPort object is invalidated.

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
typealias CFMachPortInvalidationCallBack = (CFMachPort?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFMachPort *, void *) CFMachPortInvalidationCallBack;
```

## Discussion

Your callback should free any resources allocated for `port`.

You specify this callback with [`CFMachPortSetInvalidationCallBack(_:_:)`](./cfmachportsetinvalidationcallback%28_,_%29.md).

## Parameters

- `port`: The CFMachPort object that has been invalidated.
- `info`: The `info` member of the [`CFMachPortContext`](./cfmachportcontext.md) structure used when creating `port`.

## See Also

### Callbacks
- [typealias CFMachPortCallBack](./cfmachportcallback.md)
  Callback invoked to process a message received on a CFMachPort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportinvalidationcallback)*