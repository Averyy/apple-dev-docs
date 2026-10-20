# primaryItem

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The player item that represents the primary content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
weak var primaryItem: AVPlayerItem? { get }
```

```objc
@property (nonatomic, weak, readonly) AVPlayerItem * primaryItem;
```

#### Discussion

The item must contain an [`AVAsset`](../avasset.md) that provides intrinsic mappings from its timeline to realtime dates.

## See Also

### Accessing player items
- [var templateItems: [AVPlayerItem]](./templateitems.md)
  An array of player item configurations to use as templates for player items that play interstitial content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/primaryitem)*