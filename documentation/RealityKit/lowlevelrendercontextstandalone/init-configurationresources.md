# init(configuration:resources:)

**Framework**: RealityKit  
**Kind**: init

Creates a standalone render context using resources prepared ahead of time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws
```

#### Discussion

Prefer this overload when sharing the same resources across multiple render contexts. To create a single context without prepared resources, use [`init(configuration:)`](lowlevelrendercontextstandalone/init(configuration:).md) instead.

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the context cannot be created.

## Parameters

- `configuration`: The configuration for the new context.
- `resources`: Prepared resources to use for this render context.

## See Also

- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously preparing required resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Resources needed for a render context


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/init(configuration:resources:))*