# init(configuration:)

**Framework**: RealityKit  
**Kind**: init

Creates a standalone render context, asynchronously compiling all required shader and pipeline resources.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) init(configuration: LowLevelRenderContextStandalone.Configuration) async throws
```

#### Discussion

Prefer this overload when creating a single render context. If you need to share compiled resources across multiple contexts, create a [`LowLevelRenderContextStandalone.Resources`](lowlevelrendercontextstandalone/resources.md) value first and use [`init(configuration:resources:)`](lowlevelrendercontextstandalone/init(configuration:resources:).md) instead.

> **Note**: An error if shader compilation or context creation fails.

## Parameters

- `configuration`: The Metal device and optional memory owner for the new context.

## See Also

- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](lowlevelrendercontextstandalone/init(configuration:resources:).md)
  Creates a standalone render context using pre-compiled shader and pipeline resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Pre-compiled shader and pipeline resources shared across multiple render context instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/init(configuration:))*