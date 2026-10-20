# readAdditionalContent(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Handles reading non-Core Data content in the additional content directory in the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func readAdditionalContent(from absoluteURL: URL) throws
```

```objc
- (BOOL) readAdditionalContentFromURL:(NSURL *) absoluteURL error:(NSError **) error;
```

#### Discussion

You override this method to read non-Core Data content from the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [`read(from:)`](../uidocument/read%28from%29.md).

There’s no need to invoke `super`’s implementation.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special considerations

Additional content isn’t supported on iCloud.

## Parameters

- `absoluteURL`: The URL for the additional content directory in the document’s file package.

## See Also

### Customizing read and write operations
- [func additionalContent(for: URL) throws -> Any](./additionalcontent%28for%29.md)
  Handles writing non-Core Data content to the additional content directory in the document’s file package.
- [func writeAdditionalContent(Any, to: URL, originalContentsURL: URL?) throws](./writeadditionalcontent%28_,to,originalcontentsurl%29.md)
  Handles writing non-Core Data content to the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/readadditionalcontent(from:))*