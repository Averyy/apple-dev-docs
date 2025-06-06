# binaryTarget(name:url:checksum:)

**Framework**: PackageDescription  
**Kind**: method

Creates a binary target that references a remote artifact.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func binaryTarget(name: String, url: String, checksum: String) -> Target
```

#### Discussion

Binary targets are only available on Apple platforms.

## Parameters

- `name`: The name of the target.
- `url`: The URL to the binary artifact. This URL must point to an archive   file that contains a binary artifact in its root directory.
- `checksum`: The checksum of the archive file that contains the binary   artifact.

## See Also

- [static func binaryTarget(name: String, path: String) -> Target](target/binarytarget(name:path:).md)
  Creates a binary target that references an artifact on disk.
- [var url: String?](target/url.md)
  The URL of a binary target.
- [var checksum: String?](target/checksum.md)
  The checksum for the archive file that contains the referenced binary artifact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/binarytarget(name:url:checksum:))*