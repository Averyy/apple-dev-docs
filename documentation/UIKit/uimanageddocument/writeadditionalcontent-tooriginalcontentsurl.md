# writeAdditionalContent(_:to:originalContentsURL:)

**Framework**: UIKit  
**Kind**: method

Handles writing non-Core Data content to the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func writeAdditionalContent(_ content: Any, to absoluteURL: URL, originalContentsURL absoluteOriginalContentsURL: URL?) throws
```

#### Discussion

You override this method to perform to write non-Core Data content in the additional content directory in the document’s file package. There are several issues to consider:

- You should typically implement this method only if you also implemented [`additionalContent(for:)`](uimanageddocument/additionalcontent(for:).md).
- Because this method is executed asynchronously, it’s possible that the document’s state may be different from that at which the save operation was initiated. If you need to capture the document state at save time, you should do so in [`additionalContent(for:)`](uimanageddocument/additionalcontent(for:).md).
- If you implement this method, it’s invoked automatically by [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md).
- There’s no need to invoke `super`’s implementation.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special Considerations

Additional content isn’t supported on iCloud.

## Parameters

- `content`: This is the object returned from  .
- `absoluteURL`: The URL to which to write the additional content.
- `absoluteOriginalContentsURL`: The current URL of the document that’s being saved.

## See Also

- [func readAdditionalContent(from: URL) throws](uimanageddocument/readadditionalcontent(from:).md)
  Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [func additionalContent(for: URL) throws -> Any](uimanageddocument/additionalcontent(for:).md)
  Handles writing non-Core Data content to the additional content directory in the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:))*