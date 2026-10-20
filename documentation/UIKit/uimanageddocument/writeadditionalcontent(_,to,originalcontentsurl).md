# writeAdditionalContent(_:to:originalContentsURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Handles writing non-Core Data content to the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func writeAdditionalContent(_ content: Any, to absoluteURL: URL, originalContentsURL absoluteOriginalContentsURL: URL?) throws
```

```objc
- (BOOL) writeAdditionalContent:(id) content toURL:(NSURL *) absoluteURL originalContentsURL:(NSURL *) absoluteOriginalContentsURL error:(NSError **) error;
```

#### Discussion

You override this method to perform to write non-Core Data content in the additional content directory in the document’s file package. There are several issues to consider:

- You should typically implement this method only if you also implemented [`additionalContent(for:)`](./additionalcontent%28for%29.md).
- Because this method is executed asynchronously, it’s possible that the document’s state may be different from that at which the save operation was initiated. If you need to capture the document state at save time, you should do so in [`additionalContent(for:)`](./additionalcontent%28for%29.md).
- If you implement this method, it’s invoked automatically by [`writeContents(_:andAttributes:safelyTo:for:)`](../uidocument/writecontents%28_,andattributes,safelyto,for%29.md).
- There’s no need to invoke `super`’s implementation.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special considerations

Additional content isn’t supported on iCloud.

## Parameters

- `content`: An object that represents the additional content for the document.

  This is the object returned from [`additionalContent(for:)`](./additionalcontent%28for%29.md).
- `absoluteURL`: The URL to which to write the additional content.
- `absoluteOriginalContentsURL`: The current URL of the document that’s being saved.

## See Also

### Customizing read and write operations
- [func readAdditionalContent(from: URL) throws](./readadditionalcontent%28from%29.md)
  Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [func additionalContent(for: URL) throws -> Any](./additionalcontent%28for%29.md)
  Handles writing non-Core Data content to the additional content directory in the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:))*