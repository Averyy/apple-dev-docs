# setDefaultApplication(at:toOpenURLsWithScheme:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the default app to use when opening files of a specific scheme.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setDefaultApplication(at applicationURL: URL, toOpenURLsWithScheme urlScheme: String, completion completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func setDefaultApplication(at applicationURL: URL, toOpenURLsWithScheme urlScheme: String) async throws
```

```objc
- (void) setDefaultApplicationAtURL:(NSURL *) applicationURL toOpenURLsWithScheme:(NSString *) urlScheme completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

This method sets the default app to open files of the type specified by the `urlScheme`. If a change requires user consent, the system asks the for consent asynchronously before invoking the completion handler.

## Parameters

- `applicationURL`: The URL of the default application.
- `urlScheme`: The URL of the scheme to open.
- `completionHandler`: The completion handler to call after the operation completes.

## See Also

### Setting Default Application Information
- [func setDefaultApplication(at: URL, toOpenFileAt: URL, completion: (((any Error)?) -> Void)?)](./setdefaultapplication%28at,toopenfileat,completion%29.md)
  Sets the default app to use when opening a specific file.
- [func setDefaultApplication(at: URL, toOpen: UTType, completion: (((any Error)?) -> Void)?)](./setdefaultapplication%28at,toopen,completion%29.md)
  Sets the default app to use when opening files of a specific content type.
- [func setDefaultApplication(at: URL, toOpenContentTypeOfFileAt: URL, completion: (((any Error)?) -> Void)?)](./setdefaultapplication%28at,toopencontenttypeoffileat,completion%29.md)
  Sets the default app to use when opening files of a specific content type defined by a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/setdefaultapplication(at:toopenurlswithscheme:completion:))*