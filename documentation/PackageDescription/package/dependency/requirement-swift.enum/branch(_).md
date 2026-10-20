# branch(_:)

**Framework**: PackageDescription  
**Kind**: method

Returns a requirement for a source control branch.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func branch(_ name: String) -> Package.Dependency.Requirement
```

#### Discussion

Note that packages that use branch-based dependency requirements can’t be depended upon by packages that use version-based dependency requirements; you should remove branch-based dependency requirements before publishing a version of your package.

The following example defines a version requirement that accepts any change in the develop branch.

```swift
.branch(“develop”)
```

## Parameters

- `name`: The name of the branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.enum/branch(_:))*