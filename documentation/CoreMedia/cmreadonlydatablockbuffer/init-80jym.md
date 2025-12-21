# init(_:)

**Framework**: Core Media  
**Kind**: init

Create a new block buffer referencing bytes from DispatchData. DispatchData objects consisting of multiple regions will produce a non-contiguous block buffer with each dispatch data region corresponding to a region in the block buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ dispatchData: DispatchData)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/init(_:)-80jym)*