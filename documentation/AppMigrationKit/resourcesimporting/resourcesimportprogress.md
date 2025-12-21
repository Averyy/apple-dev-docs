# resourcesImportProgress

**Framework**: AppMigrationKit  
**Kind**: property  
**Required**: Yes

A value to indicate the extension’s progress as it imports resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var resourcesImportProgress: Progress { get }
```

#### Discussion

Update this value in your implementation of [`importResources(at:request:)`](resourcesimporting/importresources(at:request:).md) as you process files in the provided directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting/resourcesimportprogress)*