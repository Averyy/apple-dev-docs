# preferredSize

**Framework**: Core Foundation  
**Kind**: property

A prototype for a function callback that determines whether there is enough free memory to satisfy a request. In implementing this function, return the actual size the allocator is likely to allocate given a request for a block of memory of size `size`. The `hint` argument is a bitfield that you should currently not use.

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
var preferredSize: CFAllocatorPreferredSizeCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/preferredsize)*