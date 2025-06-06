# readAdditionalContent(from:)

**Framework**: Uikit  
**Kind**: method

Handles reading non-Core Data content in the additional content directory in the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func readAdditionalContent(from absoluteURL: URL) throws
```

#### Discussion

You override this method to read non-Core Data content from the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [`read(from:)`](uidocument/read(from:).md).

There’s no need to invoke `super`’s implementation.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special Considerations

Additional content isn’t supported on iCloud.

## Parameters

- `absoluteURL`: The URL for the additional content directory in the document’s file package.

## See Also

- [func additionalContent(for: URL) throws -> Any](uimanageddocument/additionalcontent(for:).md)
  Handles writing non-Core Data content to the additional content directory in the document’s file package.
- [func writeAdditionalContent(Any, to: URL, originalContentsURL: URL?) throws](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md)
  Handles writing non-Core Data content to the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/readadditionalcontent(from:))*