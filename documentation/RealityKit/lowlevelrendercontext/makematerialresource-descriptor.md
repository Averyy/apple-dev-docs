# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontext/makematerialresource(descriptor:).md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makematerialresource(descriptor:))*