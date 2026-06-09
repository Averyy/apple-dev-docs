# allowedDirectoriesAndFiles

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The set of allowed directories and files that participants can access during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowedDirectoriesAndFiles: Set<URL>? { get set }
```

#### Discussion

By default, participants have restricted file system access. Use this property to specify file URLs to directories and files that should be accessible during the assessment session.

The default value is `nil`, which preserves the default unrestricted access behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/alloweddirectoriesandfiles)*