# exact(_:)

**Framework**: PackageDescription  
**Kind**: method

Returns a requirement for the given exact version.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func exact(_ version: Version) -> Package.Dependency.Requirement
```

#### Discussion

Specifying exact version requirements are not recommended as they can cause conflicts in your dependency graph when multiple other packages depend on a package. As Swift packages follow the semantic versioning convention, think about specifying a version range instead.

The following example defines a version requirement that requires version 1.2.3 of a package.

```swift
.exact(“1.2.3”)
```

## Parameters

- `version`: The exact version of the dependency for this requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.enum/exact(_:))*