# CiIssue.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe an Issues resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiIssue.Attributes
```

## Properties

- `category` (string): ​A string representing the issue’s category; for example, the name of the build phase where the issue occurred.
- `fileSource` (FileLocation): The file and line number where Xcode Cloud encountered an issue.
- `issueType` (string): A string that indicates what kind of issue Xcode Cloud encountered.
- `message` (string): Information about the issue that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciissue/attributes-data.dictionary)*