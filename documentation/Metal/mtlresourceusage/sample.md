# sample

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that enables sampling from the resource.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0 (renamed: MTLResourceUsage.read)
- iPadOS 11.0+ - Deprecated in 16.0 (renamed: MTLResourceUsage.read)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MTLResourceUsage.read)
- macOS 10.13+ - Deprecated in 13.0 (renamed: MTLResourceUsage.read)
- tvOS 11.0+ - Deprecated in 16.0 (renamed: MTLResourceUsage.read)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MTLResourceUsage.read)

## Declaration

```swift
static var sample: MTLResourceUsage { get }
```

```c
MTLResourceUsageSample
```

#### Discussion

Specify this option only if the resource is a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceusage/sample)*