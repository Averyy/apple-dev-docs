# Package.Dependency.Kind.sourceControl(name:location:requirement:)

**Framework**: PackageDescription  
**Kind**: case

A dependency based on a source control requirement.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
case sourceControl(name: String?, location: String, requirement: Package.Dependency.SourceControlRequirement)
```

## Parameters

- `name`: The name of the dependency.
- `location`: The Git URL of the dependency.
- `requirement`: The version-based requirement for a package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/kind-swift.enum/sourcecontrol(name:location:requirement:))*