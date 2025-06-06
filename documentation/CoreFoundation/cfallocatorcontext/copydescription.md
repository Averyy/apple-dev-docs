# copyDescription

**Framework**: Core Foundation  
**Kind**: property

A prototype for a function callback that provides a description of the data pointed to by the `info` field. In implementing this function, return a reference to a CFString object that describes your allocator, particularly some characteristics of your program-defined data. You may set this function pointer to `NULL`, in which case Core Foundation will provide a rudimentary description.

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
var copyDescription: CFAllocatorCopyDescriptionCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/copydescription)*