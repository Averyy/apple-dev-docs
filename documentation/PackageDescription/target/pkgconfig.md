# pkgConfig

**Framework**: PackageDescription  
**Kind**: property

The name of the package configuration file, without extension, for the system library target.

## Declaration

```swift
final let pkgConfig: String?
```

#### Discussion

If present, the Swift Package Manager tries every package configuration name separated by a space to search for the `<name>.pc` file to get the additional flags needed for the system library target.

## See Also

- [static func systemLibrary(name: String, path: String?, pkgConfig: String?, providers: [SystemPackageProvider]?) -> Target](target/systemlibrary(name:path:pkgconfig:providers:).md)
  Creates a system library target.
- [let providers: [SystemPackageProvider]?](target/providers.md)
  The providers array for a system library target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/pkgconfig)*