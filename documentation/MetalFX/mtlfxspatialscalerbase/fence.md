# fence

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional fence that you provide to synchronize your app’s untracked resources.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.13+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
var fence: (any MTLFence)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLFence> fence;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/fence)*