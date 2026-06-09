# CiIssue

**Framework**: App Store Connect API  
**Kind**: dictionary

A warning or error produced during an Xcode Cloud build action, associated with a source file location.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiIssue
```

## Topics

### Objects
- [object CiIssue.Attributes](ciissue/attributes-data.dictionary.md)
  The attributes that describe an Issues resource.

## Properties

- `attributes` (CiIssue.Attributes): The attributes that describe the Issues resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an Issues resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object FileLocation](filelocation.md)
  A source code location reference indicating the file path, line number, and column of an issue in an Xcode Cloud build.
- [object CiIssueResponse](ciissueresponse.md)
  The response body for endpoints that read a single issue from an Xcode Cloud build action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciissue)*