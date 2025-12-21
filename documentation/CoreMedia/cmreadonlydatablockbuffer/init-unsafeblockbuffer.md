# init(unsafeBlockBuffer:)

**Framework**: Core Media  
**Kind**: init

Create a readonly block buffer from an existing block buffer.

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
init(unsafeBlockBuffer: sending CMBlockBuffer)
```

#### Discussion

This init will make sure that all memory referenced by `unsafeBlockBuffer` is allocated by calling [`assureBlockMemory()`](cmblockbuffer/assureblockmemory().md).

## Parameters

- `unsafeBlockBuffer`: The   which will be subsumed by the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/init(unsafeblockbuffer:))*