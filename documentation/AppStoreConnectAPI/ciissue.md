# CiIssue

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents an Issues resource.

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
  The data structure that represents a File Locations resource.
- [object CiIssueResponse](ciissueresponse.md)
  A response that contains a single Issues resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciissue)*