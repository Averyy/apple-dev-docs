# retain

**Framework**: Core Foundation  
**Kind**: property

A prototype for a function callback that retains the data pointed to by the `info` field. In implementing this function, retain the data you have defined for the allocator context in this field. (This might make sense only if the data is a Core Foundation object.) You may set this function pointer to `NULL`.

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
var retain: CFAllocatorRetainCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/retain)*