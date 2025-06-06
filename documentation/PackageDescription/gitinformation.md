# GitInformation

**Framework**: PackageDescription  
**Kind**: struct

Information about the git status of a given package, if available.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
struct GitInformation
```

## Topics

### Instance Properties
- [let currentCommit: String](gitinformation/currentcommit.md)
  The commit currently checked out.
- [let currentTag: String?](gitinformation/currenttag.md)
  The version tag currently checked out, if available.
- [let hasUncommittedChanges: Bool](gitinformation/hasuncommittedchanges.md)
  Whether or not there are uncommitted changes in the current repository.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/gitinformation)*