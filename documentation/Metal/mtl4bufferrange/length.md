# length

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var length: UInt64
```

```c
uint64_t length;
```

## Discussion

Length of the region which begins at the given address. If the length is not known, a value of (uint64_t)-1 represents the range from the given address to the end of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4bufferrange/length)*