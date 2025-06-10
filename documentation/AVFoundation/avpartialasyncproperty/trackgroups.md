# trackGroups

**Framework**: AVFoundation  
**Kind**: property

The track groups an asset contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var trackGroups: AVAsyncProperty<Root, [AVAssetTrackGroup]> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

The value is an empty array if the asset has no track groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/trackgroups)*