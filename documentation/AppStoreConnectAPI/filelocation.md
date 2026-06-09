# FileLocation

**Framework**: App Store Connect API  
**Kind**: dictionary

A source code location reference indicating the file path, line number, and column of an issue in an Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object FileLocation
```

## Properties

- `lineNumber` (integer): The line number of a file that contains code.
- `path` (string): The path to the file that caused an issue.

## See Also

- [object CiIssue](ciissue.md)
  A warning or error produced during an Xcode Cloud build action, associated with a source file location.
- [object CiIssueResponse](ciissueresponse.md)
  The response body for endpoints that read a single issue from an Xcode Cloud build action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/filelocation)*