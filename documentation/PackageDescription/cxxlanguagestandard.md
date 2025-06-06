# CXXLanguageStandard

**Framework**: PackageDescription  
**Kind**: enum

The supported C++ language standard you use to compile C++ sources in the package.

## Declaration

```swift
enum CXXLanguageStandard
```

#### Overview

Aliases are available for some C++ language standards. For example, use `cxx98` or `cxx03` for the “ISO C++ 1998 with amendments” standard. To learn more, see [`C++ Support in Clang`](https://developer.apple.comhttps://clang.llvm.org/cxx_status.html).

## Topics

### Enumeration Cases
- [CXXLanguageStandard.cxx03](cxxlanguagestandard/cxx03.md)
  The identifier for the ISO C++ 1998 language standard with amendments.
- [CXXLanguageStandard.cxx11](cxxlanguagestandard/cxx11.md)
  The identifier for the ISO C++ 2011 language standard with amendments.
- [CXXLanguageStandard.cxx14](cxxlanguagestandard/cxx14.md)
  The identifier for the ISO C++ 2014 language standard with amendments.
- [CXXLanguageStandard.cxx1z](cxxlanguagestandard/cxx1z.md)
  The identifier for the ISO C++ 2017 language standard with amendments.
- [CXXLanguageStandard.cxx98](cxxlanguagestandard/cxx98.md)
  The identifier for the ISO C++ 1998 language standard with amendments.
- [CXXLanguageStandard.gnucxx03](cxxlanguagestandard/gnucxx03.md)
  The identifier for the ISO C++ 1998 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.gnucxx11](cxxlanguagestandard/gnucxx11.md)
  The identifier for the ISO C++ 2011 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.gnucxx14](cxxlanguagestandard/gnucxx14.md)
  The identifier for the ISO C++ 2014 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.gnucxx1z](cxxlanguagestandard/gnucxx1z.md)
  The identifier for the ISO C++ 2017 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.gnucxx98](cxxlanguagestandard/gnucxx98.md)
  The identifier for the ISO C++ 1998 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.cxx17](cxxlanguagestandard/cxx17.md)
  The identifier for the ISO C++ 2017 language standard with amendments.
- [CXXLanguageStandard.cxx20](cxxlanguagestandard/cxx20.md)
  The identifier for the ISO C++ 2020 language standard.
- [CXXLanguageStandard.cxx2b](cxxlanguagestandard/cxx2b.md)
  The identifier for the ISO C++ 2023 draft language standard.
- [CXXLanguageStandard.gnucxx17](cxxlanguagestandard/gnucxx17.md)
  The identifier for the ISO C++ 2017 language standard with amendments and GNU extensions.
- [CXXLanguageStandard.gnucxx20](cxxlanguagestandard/gnucxx20.md)
  The identifier for the ISO C++ 2020 language standard with GNU extensions.
- [CXXLanguageStandard.gnucxx2b](cxxlanguagestandard/gnucxx2b.md)
  The identifier for the ISO C++ 2023 draft language standard with GNU extensions.
### Hashing
- [func hash(into: inout Hasher)](cxxlanguagestandard/hash(into:).md)
  Hashes the C++ language standard by feeding the item into the given hasher.
- [var hashValue: Int](cxxlanguagestandard/hashvalue.md)
  The hash value for the C++ language standard.
### Operator Functions
- [static func != (Self, Self) -> Bool](cxxlanguagestandard/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Creating a Value
- [init?(rawValue: String)](cxxlanguagestandard/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Accessing the Raw Value
- [var rawValue: String](cxxlanguagestandard/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [CXXLanguageStandard.RawValue](cxxlanguagestandard/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](cxxlanguagestandard/equatable-implementations.md)
- [RawRepresentable Implementations](cxxlanguagestandard/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [typealias SwiftVersion](swiftversion.md)
  Type alias to previous name for backward source compatibility
- [enum CLanguageStandard](clanguagestandard.md)
  The supported C language standard you use to compile C sources in the package.
- [var swiftLanguageVersions: [SwiftVersion]?](package/swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`
- [var cLanguageStandard: CLanguageStandard?](package/clanguagestandard.md)
  The C language standard to use for all C targets in this package.
- [var cxxLanguageStandard: CXXLanguageStandard?](package/cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/cxxlanguagestandard)*