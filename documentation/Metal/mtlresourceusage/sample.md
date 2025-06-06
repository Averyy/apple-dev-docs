# sample

**Framework**: Metal  
**Kind**: property

An option that enables sampling from the resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var sample: MTLResourceUsage { get }
```

#### Discussion

Specify this option only if the resource is a texture.

## See Also

- [static var read: MTLResourceUsage](mtlresourceusage/read.md)
  An option that enables reading from the resource.
- [static var write: MTLResourceUsage](mtlresourceusage/write.md)
  An option that enables writing to the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceusage/sample)*