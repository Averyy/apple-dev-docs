# CiIssueResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single issue from an Xcode Cloud build action.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiIssueResponse
```

## Properties

- `data` (CiIssue) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiIssue](ciissue.md)
  A warning or error produced during an Xcode Cloud build action, associated with a source file location.
- [object FileLocation](filelocation.md)
  A source code location reference indicating the file path, line number, and column of an issue in an Xcode Cloud build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciissueresponse)*