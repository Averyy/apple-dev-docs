# CiTagPatterns.Patterns

**Framework**: App Store Connect API  
**Kind**: dictionary

A case-sensitive pattern Xcode Cloud uses to determine if a change meets tag names you configure for a workflow’s start condition.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiTagPatterns.Patterns
```

## Properties

- `isPrefix` (boolean): A Boolean value that indicates whether the pattern matches the start of a tag name, or the exact tag name.
- `pattern` (string): A case-sensitive string. If the string is a prefix pattern, Xcode Cloud starts a build when the changed tag name starts with this string. Otherwise, Xcode Cloud starts a build when the changed tag name exactly matches this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/citagpatterns/patterns-data.dictionary)*