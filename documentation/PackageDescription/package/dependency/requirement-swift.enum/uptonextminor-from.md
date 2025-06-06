# upToNextMinor(from:)

**Framework**: PackageDescription  
**Kind**: method

A source control requirement bounded to the given version’s minor version number.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func upToNextMinor(from version: Version) -> Package.Dependency.Requirement
```

#### Return Value

A source control requirement instance.

#### Discussion

Returns a requirement for a version range, starting at the given minimum version and going up to but not including the next minor version.

## Parameters

- `version`: The minimum version for the version range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.enum/uptonextminor(from:))*