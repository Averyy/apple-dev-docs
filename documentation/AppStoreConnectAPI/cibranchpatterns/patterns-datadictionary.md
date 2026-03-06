# CiBranchPatterns.Patterns

**Framework**: App Store Connect API  
**Kind**: dictionary

A case-sensitive pattern Xcode Cloud uses to determine if a change meets branch names you configure for a workflow’s start condition.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBranchPatterns.Patterns
```

## Properties

- `isPrefix` (boolean): A Boolean value that indicates whether the pattern matches the start of a branch name, or the exact branch name.
- `pattern` (string): A case-sensitive string. If the string is a prefix pattern, Xcode Cloud starts a build when the changed branch name starts with this string. Otherwise, Xcode Cloud starts a build when the changed branch name exactly matches this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibranchpatterns/patterns-data.dictionary)*