# additionalContent(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Handles writing non-Core Data content to the additional content directory in the document’s file package.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func additionalContent(for absoluteURL: URL) throws -> Any
```

```objc
- (id) additionalContentForURL:(NSURL *) absoluteURL error:(NSError **) error;
```

#### Return Value

An object that contains the additional content for the document at `absoluteURL`, or `nil` if there is a problem.

#### Discussion

You override this method to perform to manage non-Core Data content to be stored in the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [`contents(forType:)`](../uidocument/contents%28fortype%29.md). The returned object is passed to [`writeAdditionalContent(_:to:originalContentsURL:)`](./writeadditionalcontent%28_,to,originalcontentsurl%29.md).

There’s no need to invoke `super`’s implementation.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

##### Special considerations

A return value of `nil` indicates an error condition. To avoid generating an exception, you must return a value from this method. If it isn’t always the case that there will be additional content, you should return a sentinel value (for example, an [`NSNull`](../../Foundation/nsnull.md) instance) that you check for in [`writeAdditionalContent(_:to:originalContentsURL:)`](./writeadditionalcontent%28_,to,originalcontentsurl%29.md).

The object returned from this method is passed to [`writeAdditionalContent(_:to:originalContentsURL:)`](./writeadditionalcontent%28_,to,originalcontentsurl%29.md). Because [`writeAdditionalContent(_:to:originalContentsURL:)`](./writeadditionalcontent%28_,to,originalcontentsurl%29.md) is executed on a different thread, you must ensure that the object you return is thread-safe. For example, you might return an [`NSData`](../../Foundation/nsdata.md) object containing an archive of the state you want to capture.

Additional content isn’t supported on iCloud.

## Parameters

- `absoluteURL`: The URL for the additional content directory in the document’s file package.

## See Also

### Customizing read and write operations
- [func readAdditionalContent(from: URL) throws](./readadditionalcontent%28from%29.md)
  Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [func writeAdditionalContent(Any, to: URL, originalContentsURL: URL?) throws](./writeadditionalcontent%28_,to,originalcontentsurl%29.md)
  Handles writing non-Core Data content to the document’s file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/additionalcontent(for:))*