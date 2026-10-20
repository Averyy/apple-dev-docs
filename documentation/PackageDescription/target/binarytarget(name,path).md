# binaryTarget(name:path:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Creates a binary target that references an artifact on disk.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func binaryTarget(name: String, path: String) -> Target
```

#### Discussion

Binary targets are only available on Apple platforms.

## Parameters

- `name`: The name of the target.
- `path`: The path to the binary artifact. This path can point directly to a binary artifact or to an archive file that contains the binary artifact at its root.

## See Also

### Creating a Binary Target
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](./binarytarget%28name,url,checksum%29.md)
  Creates a binary target that references a remote artifact.
- [var url: String?](./url.md)
  The URL of a binary target.
- [var checksum: String?](./checksum.md)
  The checksum for the archive file that contains the referenced binary artifact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/binarytarget(name:path:))*