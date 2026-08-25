# allowedDirectoriesAndFiles

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The set of directories and files that remain visible in the Finder during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowedDirectoriesAndFiles: Set<URL>? { get set }
```

#### Discussion

Defaults to `nil`, which leaves Finder unrestricted. Setting a non-`nil` set hides everything except the given locations; pass an empty set to hide all of them.

This restricts what the Finder displays. It doesn’t sandbox participants, which can still reach other paths programmatically. Entries that aren’t file URLs are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/alloweddirectoriesandfiles)*