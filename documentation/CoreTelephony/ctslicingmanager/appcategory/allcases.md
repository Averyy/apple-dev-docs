# allCases

**Framework**: Core Telephony  
**Kind**: property

All application categories supported at the current OS version.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
static var allCases: [CTSlicingManager.AppCategory] { get }
```

#### Discussion

On iOS 26.3 and later, this property returns `[.gaming, .communication, .streaming]`. On iOS 27.0 and later, this property also includes `.missionCritical`.

Use this property to enumerate all valid categories at runtime without checking the OS version directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/appcategory/allcases)*