# cLanguageStandard

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The C language standard to use for all C targets in this package.

## Declaration

```swift
final var cLanguageStandard: CLanguageStandard?
```

## See Also

### Declaring Supported Languages
- [enum SwiftLanguageMode](../swiftlanguagemode.md)
  The Swift language mode used to compile Swift sources in the package
- [enum CLanguageStandard](../clanguagestandard.md)
  The supported C language standard you use to compile C sources in the package.
- [enum CXXLanguageStandard](../cxxlanguagestandard.md)
  The supported C++ language standard you use to compile C++ sources in the package.
- [var swiftLanguageModes: [SwiftLanguageMode]?](./swiftlanguagemodes.md)
  The list of Swift language modes with which this package is compatible.
- [var cxxLanguageStandard: CXXLanguageStandard?](./cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.
- [typealias SwiftVersion](../swiftversion.md)
  Type alias to previous name for backward source compatibility
- [var swiftLanguageVersions: [SwiftVersion]?](./swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/clanguagestandard)*