# AVMakeRect(aspectRatio:insideRect:)

**Framework**: AVFoundation  
**Kind**: func

Returns a scaled rectangle that maintains the specified aspect ratio within a bounding rectangle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AVMakeRect(aspectRatio: CGSize, insideRect boundingRect: CGRect) -> CGRect
```

#### Return Value

Returns a scaled `CGRect` that maintains the aspect ratio specified by `aspectRatio` that fits within `boundingRect`.

#### Discussion

Use this function when attempting to fit the presentation size of a player item object’s content within the bounds of another [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer). Use the returned [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) as the player layer’s [`frame`](https://developer.apple.com/documentation/QuartzCore/CALayer/frame) property value. For example:

**Swift**:

```swift
let aspectRatio = CGSize(width: 1920, height: 1080)
playerLayer.frame = AVMakeRect(aspectRatio: aspectRatio, insideRect: superLayer.bounds)
```

**Objective-C**:

```objc
CGSize aspectRatio = CGSizeMake(1920, 1080);
self.playerLayer.frame = AVMakeRectWithAspectRatioInsideRect(aspectRatio, self.superLayer.bounds);
```

## Parameters

- `aspectRatio`: The width and height ratio (aspect ratio) you want to maintain.
- `boundingRect`: The bounding rectangle you want to fit into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmakerect(aspectratio:insiderect:))*