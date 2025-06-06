# dispatch_data_t

**Framework**: Dispatch  
**Kind**: typealias

An immutable object representing a contiguous or sparse region of memory.

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
typealias dispatch_data_t = __DispatchData
```

#### Discussion

Any direct access to the memory in a dispatch data object must not modify that memory.

In 64-bit apps, you may cast a [`dispatch_data_t`](dispatch_data_t.md) type to an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object. However, you may not perform a reverse cast — that is, cast an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object to a [`dispatch_data_t`](dispatch_data_t.md) type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_t)*