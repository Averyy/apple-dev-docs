# resources

**Framework**: PackageDescription  
**Kind**: property

The explicit list of resource files in the target.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
final var resources: [Resource]?
```

## See Also

- [var path: String?](target/path.md)
  The path of the target, relative to the package root.
- [var exclude: [String]](target/exclude.md)
  The paths to source and resource files that you don’t want to include in the target.
- [var sources: [String]?](target/sources.md)
  The source files in this target.
- [struct Resource](resource.md)
  A resource to bundle with the Swift package.
- [var publicHeadersPath: String?](target/publicheaderspath.md)
  The path to the directory that contains public headers of a C-family target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/resources)*