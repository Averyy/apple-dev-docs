# swiftLanguageModes

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The list of Swift language modes with which this package is compatible.

## Declaration

```swift
final var swiftLanguageModes: [SwiftLanguageMode]?
```

## See Also

### Declaring Supported Languages
- [enum SwiftLanguageMode](../swiftlanguagemode.md)
  The Swift language mode used to compile Swift sources in the package
- [enum CLanguageStandard](../clanguagestandard.md)
  The supported C language standard you use to compile C sources in the package.
- [enum CXXLanguageStandard](../cxxlanguagestandard.md)
  The supported C++ language standard you use to compile C++ sources in the package.
- [var cLanguageStandard: CLanguageStandard?](./clanguagestandard.md)
  The C language standard to use for all C targets in this package.
- [var cxxLanguageStandard: CXXLanguageStandard?](./cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.
- [typealias SwiftVersion](../swiftversion.md)
  Type alias to previous name for backward source compatibility
- [var swiftLanguageVersions: [SwiftVersion]?](./swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/swiftlanguagemodes)*