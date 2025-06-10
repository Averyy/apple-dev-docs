# writeTimestamp(granularity:after:counterHeap:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Writes a GPU timestamp into the given [`MTL4CounterHeap`](mtl4counterheap.md) at `index` after `stage` completes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func writeTimestamp(granularity: MTL4TimestampGranularity, after stage: MTLRenderStages, counterHeap: any MTL4CounterHeap, index: Int)
```

#### Discussion

This command only guarantees all draws prior to this command are complete when Metal writes the timestamp into the counter heap you provide in the `counterHeap` parameter. The timestamp may also include subsequent operations.

If you call this method before any draw calls, Metal writes a timestamp before the stage you specify in the `stage` parameter begins.

## Parameters

- `granularity`: A   hint.
- `stage`:   that need to complete before Metal writes the timestamp. This may also include later   stages that are related, for example   may include   .
- `counterHeap`:   into which Metal writes timestamps.
- `index`: The index value into which Metal writes this timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:))*