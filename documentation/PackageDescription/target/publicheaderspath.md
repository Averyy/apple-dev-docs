# publicHeadersPath

**Framework**: PackageDescription  
**Kind**: property

The path to the directory that contains public headers of a C-family target.

## Declaration

```swift
final var publicHeadersPath: String?
```

#### Discussion

If this is `nil`, the directory is set to `include`.

## See Also

- [var path: String?](target/path.md)
  The path of the target, relative to the package root.
- [var exclude: [String]](target/exclude.md)
  The paths to source and resource files that you don’t want to include in the target.
- [var sources: [String]?](target/sources.md)
  The source files in this target.
- [var resources: [Resource]?](target/resources.md)
  The explicit list of resource files in the target.
- [struct Resource](resource.md)
  A resource to bundle with the Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/publicheaderspath)*