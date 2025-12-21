# CLanguageStandard

**Framework**: PackageDescription  
**Kind**: enum

The supported C language standard you use to compile C sources in the package.

## Declaration

```swift
enum CLanguageStandard
```

## Topics

### Enumeration Cases
- [CLanguageStandard.c11](clanguagestandard/c11.md)
  The identifier for the ISO C 2011 language standard.
- [CLanguageStandard.c17](clanguagestandard/c17.md)
  The identifier for the ISO C 2017 language stadard.
- [CLanguageStandard.c18](clanguagestandard/c18.md)
  The identifier for the ISO C 2017 language standard.
- [CLanguageStandard.c2x](clanguagestandard/c2x.md)
  The identifier for the ISO C2x draft language standard.
- [CLanguageStandard.c89](clanguagestandard/c89.md)
  The identifier for the ISO C 1989 language standard.
- [CLanguageStandard.c90](clanguagestandard/c90.md)
  The identifier for the ISO C 1990 language standard.
- [CLanguageStandard.c99](clanguagestandard/c99.md)
  The identifier for the ISO C 1999 language standard.
- [CLanguageStandard.gnu11](clanguagestandard/gnu11.md)
  The identifier for the ISO C 2011 language standard with GNU extensions.
- [CLanguageStandard.gnu17](clanguagestandard/gnu17.md)
  The identifier for the ISO C 2017 language standard with GNU extensions.
- [CLanguageStandard.gnu18](clanguagestandard/gnu18.md)
  The identifier for the ISO C 2017 language standard with GNU extensions.
- [CLanguageStandard.gnu2x](clanguagestandard/gnu2x.md)
  The identifier for the ISO C2x draft language standard with GNU extensions.
- [CLanguageStandard.gnu89](clanguagestandard/gnu89.md)
  The identifier for the ISO C 1990 language standard with GNU extensions.
- [CLanguageStandard.gnu90](clanguagestandard/gnu90.md)
  The identifier for the ISO C 1990 language standard with GNU extensions.
- [CLanguageStandard.gnu99](clanguagestandard/gnu99.md)
  The identifier for the ISO C 1999 language standard with GNU extensions.
- [CLanguageStandard.iso9899_1990](clanguagestandard/iso9899_1990.md)
  The identifier for the ISO C 1990 language standard.
- [CLanguageStandard.iso9899_199409](clanguagestandard/iso9899_199409.md)
  The identifier for the ISO C 1990 language standard with amendment 1.
- [CLanguageStandard.iso9899_1999](clanguagestandard/iso9899_1999.md)
  The identifier for the ISO C 1999 language standard.
- [CLanguageStandard.iso9899_2011](clanguagestandard/iso9899_2011.md)
  The identifier for the ISO C 2011 language standard.
- [CLanguageStandard.iso9899_2017](clanguagestandard/iso9899_2017.md)
  The identifier for the ISO C 2017 language standard.
- [CLanguageStandard.iso9899_2018](clanguagestandard/iso9899_2018.md)
  The identifier for the ISO C 2017 language standard.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum SwiftLanguageMode](swiftlanguagemode.md)
  The Swift language mode used to compile Swift sources in the package
- [enum CXXLanguageStandard](cxxlanguagestandard.md)
  The supported C++ language standard you use to compile C++ sources in the package.
- [var swiftLanguageModes: [SwiftLanguageMode]?](package/swiftlanguagemodes.md)
  The list of Swift language modes with which this package is compatible.
- [var cLanguageStandard: CLanguageStandard?](package/clanguagestandard.md)
  The C language standard to use for all C targets in this package.
- [var cxxLanguageStandard: CXXLanguageStandard?](package/cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.
- [typealias SwiftVersion](swiftversion.md)
  Type alias to previous name for backward source compatibility
- [var swiftLanguageVersions: [SwiftVersion]?](package/swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/clanguagestandard)*