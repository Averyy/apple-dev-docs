# SwiftVersion

**Framework**: PackageDescription  
**Kind**: typealias

Type alias to previous name for backward source compatibility

**Availability**:
- SwiftPM ?+

## Declaration

```swift
typealias SwiftVersion = SwiftLanguageMode
```

## See Also

- [enum SwiftLanguageMode](swiftlanguagemode.md)
  The Swift language mode used to compile Swift sources in the package
- [enum CLanguageStandard](clanguagestandard.md)
  The supported C language standard you use to compile C sources in the package.
- [enum CXXLanguageStandard](cxxlanguagestandard.md)
  The supported C++ language standard you use to compile C++ sources in the package.
- [var swiftLanguageModes: [SwiftLanguageMode]?](package/swiftlanguagemodes.md)
  The list of Swift language modes with which this package is compatible.
- [var cLanguageStandard: CLanguageStandard?](package/clanguagestandard.md)
  The C language standard to use for all C targets in this package.
- [var cxxLanguageStandard: CXXLanguageStandard?](package/cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.
- [var swiftLanguageVersions: [SwiftVersion]?](package/swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftversion)*