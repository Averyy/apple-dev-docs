# SwiftLanguageMode

**Framework**: PackageDescription  
**Kind**: enum

The Swift language mode used to compile Swift sources in the package

## Declaration

```swift
enum SwiftLanguageMode
```

## Topics

### Swift Language Modes
- [SwiftLanguageMode.v6](swiftlanguagemode/v6.md)
  The identifier for the Swift 6 language version.
- [SwiftLanguageMode.v5](swiftlanguagemode/v5.md)
  The identifier for the Swift 5 language version.
- [SwiftLanguageMode.v4_2](swiftlanguagemode/v4_2.md)
  The identifier for the Swift 4.2 language version.
- [SwiftLanguageMode.v4](swiftlanguagemode/v4.md)
  The identifier for the Swift 4 language version.
- [SwiftLanguageMode.version(_:)](swiftlanguagemode/version(_:).md)
  A user-defined value for the Swift version.
- [SwiftLanguageMode.v3](swiftlanguagemode/v3.md)
  The identifier for the Swift 3 language version.
### Default Implementations
- [CustomStringConvertible Implementations](swiftlanguagemode/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

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
- [typealias SwiftVersion](swiftversion.md)
  Type alias to previous name for backward source compatibility
- [var swiftLanguageVersions: [SwiftVersion]?](package/swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftlanguagemode)*