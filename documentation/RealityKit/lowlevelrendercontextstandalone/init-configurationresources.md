# init(configuration:resources:)

**Framework**: RealityKit  
**Kind**: init

Creates a standalone render context using pre-compiled shader and pipeline resources.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws
```

#### Discussion

Prefer this overload when sharing compiled resources across multiple render contexts. To create a single context without pre-compiling resources, use [`init(configuration:)`](lowlevelrendercontextstandalone/init(configuration:).md) instead.

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the context cannot be created.

## Parameters

- `configuration`: The Metal device and optional memory owner for the new context.
- `resources`: Pre-compiled shader and pipeline resources to share across render contexts.

## See Also

- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously compiling all required shader and pipeline resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Pre-compiled shader and pipeline resources shared across multiple render context instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/init(configuration:resources:))*