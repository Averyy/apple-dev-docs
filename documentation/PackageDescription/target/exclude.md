# exclude

**Framework**: PackageDescription  
**Kind**: property

The paths to source and resource files that you don’t want to include in the target.

## Declaration

```swift
final var exclude: [String]
```

#### Discussion

Excluded paths are relative to the target path. This property has precedence over the `sources` and `resources` properties.

## See Also

- [var path: String?](target/path.md)
  The path of the target, relative to the package root.
- [var sources: [String]?](target/sources.md)
  The source files in this target.
- [var resources: [Resource]?](target/resources.md)
  The explicit list of resource files in the target.
- [struct Resource](resource.md)
  A resource to bundle with the Swift package.
- [var publicHeadersPath: String?](target/publicheaderspath.md)
  The path to the directory that contains public headers of a C-family target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/exclude)*