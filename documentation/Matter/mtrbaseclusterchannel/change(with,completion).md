# change(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func change(with params: MTRChannelClusterChangeChannelParams, completion: @escaping @Sendable (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)
```

```swift
func change(with params: MTRChannelClusterChangeChannelParams) async throws -> MTRChannelClusterChangeChannelResponseParams
```

```objc
- (void) changeChannelWithParams:(MTRChannelClusterChangeChannelParams *) params completion:(void (^)(MTRChannelClusterChangeChannelResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel/change(with:completion:))*