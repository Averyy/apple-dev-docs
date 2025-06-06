# renameDocument(at:proposedName:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Renames a document at the specified URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func renameDocument(at documentURL: URL, proposedName: String) async throws -> URL
```

## Parameters

- `documentURL`: The URL specifying the location of the document.
- `proposedName`: The proposed new name to rename the document to. If   is already taken, the system might alter the proposed name and confirm the new suggestion with the user. The final name that the system chooses appears in the   parameter of  .
- `completionHandler`: A completion handler to execute after the renaming operation occurs. The final URL and error information are available in the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/renamedocument(at:proposedname:completionhandler:))*