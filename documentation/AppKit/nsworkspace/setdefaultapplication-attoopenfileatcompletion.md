# setDefaultApplication(at:toOpenFileAt:completion:)

**Framework**: AppKit  
**Kind**: method

Sets the default app to use when opening a specific file.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setDefaultApplication(at applicationURL: URL, toOpenFileAt url: URL) async throws
```

#### Discussion

This method sets the default app to use for a specific file (rather than all files of that content type). The system requires write access to the specified `url` before it can make the change.

If a change requires user consent, the system asks the user for consent asynchronously before invoking the completion handler.

This function doesn’t apply to non-file URLs.

## Parameters

- `applicationURL`: The URL of the default app to use when opening the file.
- `url`: The URL of the file to open.
- `completionHandler`: The completion handler to call after the operation completes.

## See Also

- [func setDefaultApplication(at: URL, toOpen: UTType, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopen:completion:).md)
  Sets the default app to use when opening files of a specific content type.
- [func setDefaultApplication(at: URL, toOpenContentTypeOfFileAt: URL, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopencontenttypeoffileat:completion:).md)
  Sets the default app to use when opening files of a specific content type defined by a file URL.
- [func setDefaultApplication(at: URL, toOpenURLsWithScheme: String, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopenurlswithscheme:completion:).md)
  Sets the default app to use when opening files of a specific scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/setdefaultapplication(at:toopenfileat:completion:))*