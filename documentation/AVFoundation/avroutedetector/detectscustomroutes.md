# detectsCustomRoutes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether route detection includes custom routes.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: To detect custom routes, adopt the [AVSystemRouting](../../AVSystemRouting/AVSystemRouting.md) framework instead.

## Declaration

```swift
var detectsCustomRoutes: Bool { get set }
```

```objc
@property (nonatomic) BOOL detectsCustomRoutes;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Only set it to [`true`](../../Swift/true.md) if your app uses an instance of [`AVCustomRoutingController`](../../AVRouting/avcustomroutingcontroller.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/detectscustomroutes)*