# init(device:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously compiles the shared shader and pipeline resources for the given device.

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

> **Note**: An error if shader compilation fails.

## Parameters

- `device`: The Metal device to allocate and compile resources on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/resources/init(device:))*