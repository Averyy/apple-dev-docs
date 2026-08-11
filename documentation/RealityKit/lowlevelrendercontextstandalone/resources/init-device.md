# init(device:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously prepare resources for the given device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) init(device: any MTLDevice) async throws
```

#### Discussion

> **Note**: An error if resources preparation fails.

## Parameters

- `device`: The Metal device to prepare resources using.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/resources/init(device:))*