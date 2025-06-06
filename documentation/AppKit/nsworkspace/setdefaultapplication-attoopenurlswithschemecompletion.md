# setDefaultApplication(at:toOpenURLsWithScheme:completion:)

**Framework**: AppKit  
**Kind**: method

Sets the default app to use when opening files of a specific scheme.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setDefaultApplication(at applicationURL: URL, toOpenURLsWithScheme urlScheme: String) async throws
```

#### Discussion

This method sets the default app to open files of the type specified by the `urlScheme`. If a change requires user consent, the system asks the for consent asynchronously before invoking the completion handler.

## Parameters

- `applicationURL`: The URL of the default application.
- `urlScheme`: The URL of the scheme to open.
- `completionHandler`: The completion handler to call after the operation completes.

## See Also

- [func setDefaultApplication(at: URL, toOpenFileAt: URL, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopenfileat:completion:).md)
  Sets the default app to use when opening a specific file.
- [func setDefaultApplication(at: URL, toOpen: UTType, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopen:completion:).md)
  Sets the default app to use when opening files of a specific content type.
- [func setDefaultApplication(at: URL, toOpenContentTypeOfFileAt: URL, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopencontenttypeoffileat:completion:).md)
  Sets the default app to use when opening files of a specific content type defined by a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/setdefaultapplication(at:toopenurlswithscheme:completion:))*