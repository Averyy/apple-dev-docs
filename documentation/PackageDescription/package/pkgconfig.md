# pkgConfig

**Framework**: PackageDescription  
**Kind**: property

The name to use for C modules.

## Declaration

```swift
final var pkgConfig: String?
```

#### Discussion

If present, the Swift Package Manager searches for a `<name>.pc` file to get the required additional flags for a system target.

## See Also

- [enum SystemPackageProvider](systempackageprovider.md)
  The system package providers that this package uses.
- [var providers: [SystemPackageProvider]?](package/providers.md)
  An array of providers for a system target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/pkgconfig)*