# Context

**Framework**: PackageDescription  
**Kind**: struct

The context information for a Swift package.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
struct Context
```

#### Overview

The context encapsulates states that are known when Swift Package Manager interprets the package manifest, for example the location in the file system where the current package resides.

## Topics

### Type Properties
- [static var environment: [String : String]](context/environment.md)
  Snapshot of the system environment variables.
- [static var gitInformation: GitInformation?](context/gitinformation.md)
  Information about the git status of a given package, if available.
- [static var packageDirectory: String](context/packagedirectory.md)
  The directory that contains `Package.swift`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [class Package](package.md)
  The configuration of a Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/context)*