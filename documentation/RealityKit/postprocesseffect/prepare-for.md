# prepare(for:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

A method where you can prepare the metal device with initial setup work.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func prepare(for device: any MTLDevice)
```

#### Discussion

When you set or update the [`customPostProcessing`](realityviewrenderingeffects/custompostprocessing.md) property, RealityKit calls this method once, after it does its setup work, but before rendering the next frame.

Adding long-running tasks in this method may cause rendering hitches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/postprocesseffect/prepare(for:))*