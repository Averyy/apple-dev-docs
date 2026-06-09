# CiStartConditionFileMatcher

**Framework**: App Store Connect API  
**Kind**: dictionary

A path pattern filter applied to an Xcode Cloud workflow start condition, restricting triggers to changes in specific files or directories.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiStartConditionFileMatcher
```

## Properties

- `directory` (string): The directory you configure for a custom start condition’s Files and Folders setting.
- `fileExtension` (string): The file extension you configure for a custom start condition’s Files and Folders setting.
- `fileName` (string): The filename you configure for a custom start condition’s Files and Folders setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cistartconditionfilematcher)*