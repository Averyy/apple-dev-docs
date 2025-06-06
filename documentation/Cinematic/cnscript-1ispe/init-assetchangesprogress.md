# init(asset:changes:progress:)

**Framework**: Cinematic  
**Kind**: init

Creates a Cinematic script based on a movie and applying changes to the movie.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
init(asset: AVAsset, changes: CNScript.Changes? = nil, progress: Progress? = nil) async throws
```

## Parameters

- `asset`: The original movie.
- `changes`: Changes to apply to the original script.
- `progress`: The optional progress object to track progress or cancel loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/init(asset:changes:progress:))*