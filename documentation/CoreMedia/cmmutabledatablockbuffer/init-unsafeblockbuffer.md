# init(unsafeBlockBuffer:)

**Framework**: Core Media  
**Kind**: init

Creates a mutable block buffer from an existing block buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(unsafeBlockBuffer: sending CMBlockBuffer)
```

#### Discussion

This init will make sure that all memory referenced by `unsafeBlockBuffer` is allocated by calling [`assureBlockMemory()`](cmblockbuffer/assureblockmemory().md).

## Parameters

- `unsafeBlockBuffer`: The   which will be subsumed by the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/init(unsafeblockbuffer:))*