# checksum

**Framework**: PackageDescription  
**Kind**: property

The checksum for the archive file that contains the referenced binary artifact.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
final var checksum: String?
```

#### Discussion

If you make a remote binary framework available as a Swift package, declare a remote, or , binary target in your package manifest with [`binaryTarget(name:url:checksum:)`](target/binarytarget(name:url:checksum:).md). Always run `swift package compute-checksum path/to/MyFramework.zip` at the command line to make sure you create a correct SHA256 checksum.

For more information, see doc:distributing-binary-frameworks-as-swift-packages.

## See Also

- [static func binaryTarget(name: String, path: String) -> Target](target/binarytarget(name:path:).md)
  Creates a binary target that references an artifact on disk.
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](target/binarytarget(name:url:checksum:).md)
  Creates a binary target that references a remote artifact.
- [var url: String?](target/url.md)
  The URL of a binary target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/checksum)*