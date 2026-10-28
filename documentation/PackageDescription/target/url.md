# url

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The URL of a binary target.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
final var url: String?
```

## Discussion

The URL points to an archive file that contains the referenced binary artifact at its root.

Binary targets are only available on Apple platforms.

## See Also

### Creating a Binary Target
- [static func binaryTarget(name: String, path: String) -> Target](./binarytarget%28name,path%29.md)
  Creates a binary target that references an artifact on disk.
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](./binarytarget%28name,url,checksum%29.md)
  Creates a binary target that references a remote artifact.
- [var checksum: String?](./checksum.md)
  The checksum for the archive file that contains the referenced binary artifact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/url)*