# read(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reads the document data in a file at a specified location in the application sandbox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func read(from url: URL) throws
```

```objc
- (BOOL) readFromURL:(NSURL *) url error:(NSError **) outError;
```

#### Discussion

Typical [`UIDocument`](../uidocument.md) subclasses shouldn’t need to call this method directly, especially if the entire file is read at once. The default implementation calls [`load(fromContents:ofType:)`](./load%28fromcontents,oftype%29.md) on the queue on which [`open(completionHandler:)`](./open%28completionhandler%29.md) was called to provide the `UIDocument` subclass with the document data object.

Subclasses that want more control over the reading of the document file—for example, that want to read a large document file incrementally—can override this method. It isn’t necessary for these subclasses to call the superclass implementation (`super`).

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: A file URL that identifies the location of the document file in the application sandbox. This file URL is typically the one returned by the [`fileURL`](./fileurl.md) property.

## See Also

### Reading document data
- [func open(completionHandler: ((Bool) -> Void)?)](./open%28completionhandler%29.md)
  Opens a document asynchronously.
- [func load(fromContents: Any, ofType: String?) throws](./load%28fromcontents,oftype%29.md)
  Loads the document data into the app’s data model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/read(from:))*