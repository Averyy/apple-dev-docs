# dispatch_data_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

An immutable object representing a contiguous or sparse region of memory.

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
typealias dispatch_data_t = __DispatchData
```

```c
typedef NSObject<OS_dispatch_data> * dispatch_data_t;
```

#### Discussion

Any direct access to the memory in a dispatch data object must not modify that memory.

In 64-bit apps, you may cast a [`dispatch_data_t`](./dispatch_data_t.md) type to an [`NSData`](../Foundation/nsdata.md) object. However, you may not perform a reverse cast — that is, cast an [`NSData`](../Foundation/nsdata.md) object to a [`dispatch_data_t`](./dispatch_data_t.md) type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_t)*