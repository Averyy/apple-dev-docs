# executePlan()

**Framework**: AVFoundation  
**Kind**: method

Starts the incremental segment writing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func executePlan() async throws -> AVComposition
```

#### Return Value

The assembly composition containing all completed segments from all tracks.

#### Discussion

The planner calls every segment handler sequentially, starting with the first one available, or at the next unfinished segment if resuming a previously canceled session. Upon success (no error thrown), this means that all segments for all tracks have been completed. The returned assemblyComposition can be used to put the incremental tracks back together. One way to accomplish this is by feeding the assemblyComposition through AVAssetExportSession with the pass-through preset. The client is responsible for combining any other tracks (those that were not eligible for incremental writing), as well as establishing any track references between the incrementally written tracks and the other tracks in the final asset.

> **Note**: An error if the export fails or if a segment handler reports an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/executeplan())*