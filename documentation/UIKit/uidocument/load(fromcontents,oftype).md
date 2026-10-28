# load(fromContents:ofType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Loads the document data into the app’s data model.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func load(fromContents contents: Any, ofType typeName: String?) throws
```

```objc
- (BOOL) loadFromContents:(id) contents ofType:(NSString *) typeName error:(NSError **) outError;
```

## Discussion

Override this method to accept and load the data for a document. After `UIDocument` reads the document data from the file located at [`fileURL`](./fileurl.md) it calls your subclass, passing the data to the subclass in this method. This method is called on the queue that the [`open(completionHandler:)`](./open%28completionhandler%29.md) method was called on (typically, the main queue).

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `contents`: An object encapsulating the document data to load. This object is either an instance of the [`NSData`](../../Foundation/nsdata.md) class (for flat files) or the [`FileWrapper`](../../Foundation/filewrapper.md) class (for file packages).
- `typeName`: The file type of the document, a Uniform Type Identifier (UTI) based on the file extension of [`fileURL`](./fileurl.md). You can obtain the default value of the file type from the [`fileType`](./filetype.md) property.

## See Also

### Reading document data
- [func open(completionHandler: ((Bool) -> Void)?)](./open%28completionhandler%29.md)
  Opens a document asynchronously.
- [func read(from: URL) throws](./read%28from%29.md)
  Reads the document data in a file at a specified location in the application sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/load(fromcontents:oftype:))*