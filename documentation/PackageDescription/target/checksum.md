# checksum

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The checksum for the archive file that contains the referenced binary artifact.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
final var checksum: String?
```

#### Discussion

If you make a remote binary framework available as a Swift package, declare a remote, or *URL-based*, binary target in your package manifest with [`binaryTarget(name:url:checksum:)`](./binarytarget%28name,url,checksum%29.md). Always run `swift package compute-checksum path/to/MyFramework.zip` at the command line to make sure you create a correct SHA256 checksum.

For more information, see [Distributing binary frameworks as Swift packages](../../Xcode/distributing-binary-frameworks-as-swift-packages.md).

## See Also

### Creating a Binary Target
- [static func binaryTarget(name: String, path: String) -> Target](./binarytarget%28name,path%29.md)
  Creates a binary target that references an artifact on disk.
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](./binarytarget%28name,url,checksum%29.md)
  Creates a binary target that references a remote artifact.
- [var url: String?](./url.md)
  The URL of a binary target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/checksum)*