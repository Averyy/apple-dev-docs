# trackGroups

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The track groups an asset contains.

**Availability**:
- iOS 7.0+ - Deprecated in 16.0
- iPadOS 7.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.9+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`trackGroups`](../avpartialasyncproperty/trackgroups.md) asynchronously instead.

## Declaration

```swift
var trackGroups: [AVAssetTrackGroup] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetTrackGroup *> * trackGroups;
```

## Discussion

This value is an empty array if the asset has no track groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/trackgroups)*