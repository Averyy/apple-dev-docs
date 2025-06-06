# additionalContent(for:)

**Framework**: Uikit  
**Kind**: method

Handles writing non-Core Data content to the additional content directory in the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func additionalContent(for absoluteURL: URL) throws -> Any
```

#### Return Value

An object that contains the additional content for the document at `absoluteURL`, or `nil` if there is a problem.

#### Discussion

You override this method to perform to manage non-Core Data content to be stored in the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [`contents(forType:)`](uidocument/contents(fortype:).md). The returned object is passed to [`writeAdditionalContent(_:to:originalContentsURL:)`](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md).

There’s no need to invoke `super`’s implementation.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special Considerations

A return value of `nil` indicates an error condition. To avoid generating an exception, you must return a value from this method. If it isn’t always the case that there will be additional content, you should return a sentinel value (for example, an [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) instance) that you check for in [`writeAdditionalContent(_:to:originalContentsURL:)`](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md).

The object returned from this method is passed to [`writeAdditionalContent(_:to:originalContentsURL:)`](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md). Because [`writeAdditionalContent(_:to:originalContentsURL:)`](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md) is executed on a different thread, you must ensure that the object you return is thread-safe. For example, you might return an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing an archive of the state you want to capture.

Additional content isn’t supported on iCloud.

## Parameters

- `absoluteURL`: The URL for the additional content directory in the document’s file package.

## See Also

- [func readAdditionalContent(from: URL) throws](uimanageddocument/readadditionalcontent(from:).md)
  Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [func writeAdditionalContent(Any, to: URL, originalContentsURL: URL?) throws](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md)
  Handles writing non-Core Data content to the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/additionalcontent(for:))*