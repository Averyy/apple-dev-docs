# region

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The region in which the caption exists.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```swift
var region: AVCaptionRegion? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVCaptionRegion * region;
```

## Discussion

This property is `nil` when the underlying caption format doesn’t support or use regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/region)*