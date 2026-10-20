# providers

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The providers array for a system library target.

## Declaration

```swift
final let providers: [SystemPackageProvider]?
```

## See Also

### Creating a System Library Target
- [static func systemLibrary(name: String, path: String?, pkgConfig: String?, providers: [SystemPackageProvider]?) -> Target](./systemlibrary%28name,path,pkgconfig,providers%29.md)
  Creates a system library target.
- [let pkgConfig: String?](./pkgconfig.md)
  The name of the package configuration file, without extension, for the system library target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/providers)*