# url

**Framework**: PackageDescription  
**Kind**: property

The URL of a binary target.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
final var url: String?
```

#### Discussion

The URL points to an archive file that contains the referenced binary artifact at its root.

Binary targets are only available on Apple platforms.

## See Also

- [static func binaryTarget(name: String, path: String) -> Target](target/binarytarget(name:path:).md)
  Creates a binary target that references an artifact on disk.
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](target/binarytarget(name:url:checksum:).md)
  Creates a binary target that references a remote artifact.
- [var checksum: String?](target/checksum.md)
  The checksum for the archive file that contains the referenced binary artifact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/url)*