# upToNextMajor(from:)

**Framework**: PackageDescription  
**Kind**: method

A source control requirement bounded to the given version’s major version number.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func upToNextMajor(from version: Version) -> Package.Dependency.Requirement
```

#### Return Value

A source control requirement instance.

#### Discussion

Returns a requirement for a version range, starting at the given minimum version and going up to but not including the next major version. This is the recommended version requirement.

## Parameters

- `version`: The minimum version for the version range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.enum/uptonextmajor(from:))*