# canRequestDownloads

**Framework**: Translation  
**Kind**: property

Whether this session is able to present UI to request downloading languages if they’re not already installed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var canRequestDownloads: Bool { get }
```

#### Discussion

Sessions created using `.translationTask()` can always request downloads, but sessions created directly cannot request downloads, and will throw an error if the languages aren’t installed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/canrequestdownloads)*