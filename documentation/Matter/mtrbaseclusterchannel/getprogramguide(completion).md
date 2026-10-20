# getProgramGuide(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func getProgramGuide(completion: @escaping @Sendable (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)
```

```swift
func programGuide() async throws -> MTRChannelClusterProgramGuideResponseParams
```

```objc
- (void) getProgramGuideWithCompletion:(void (^)(MTRChannelClusterProgramGuideResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel/getprogramguide(completion:))*