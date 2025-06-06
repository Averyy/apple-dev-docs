# path

**Framework**: PackageDescription  
**Kind**: property

The path of the target, relative to the package root.

## Declaration

```swift
final var path: String?
```

#### Discussion

If the path is `nil`, Swift Package Manager looks for a target’s source files at predefined search paths and in a subdirectory with the target’s name.

The predefined search paths are the following directories under the package root:

- `Sources`, `Source`, `src`, and `srcs` for regular targets
- `Tests`, `Sources`, `Source`, `src`, and `srcs` for test targets

For example, Swift Package Manager looks for source files inside the `[PackageRoot]/Sources/[TargetName]` directory.

Don’t escape the package root; that is, values like `../Foo` or `/Foo` are invalid.

## See Also

- [var exclude: [String]](target/exclude.md)
  The paths to source and resource files that you don’t want to include in the target.
- [var sources: [String]?](target/sources.md)
  The source files in this target.
- [var resources: [Resource]?](target/resources.md)
  The explicit list of resource files in the target.
- [struct Resource](resource.md)
  A resource to bundle with the Swift package.
- [var publicHeadersPath: String?](target/publicheaderspath.md)
  The path to the directory that contains public headers of a C-family target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/path)*