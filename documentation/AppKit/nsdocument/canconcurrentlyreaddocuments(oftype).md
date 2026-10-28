# canConcurrentlyReadDocuments(ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func canConcurrentlyReadDocuments(ofType typeName: String) -> Bool
```

```objc
+ (BOOL) canConcurrentlyReadDocumentsOfType:(NSString *) typeName;
```

## Return Value

[`false`](../../Swift/false.md) by default; subclasses can override to return [`true`](../../Swift/true.md), thereby causing documents of the specified type to be read concurrently.

## Discussion

Your [`NSDocument`](../nsdocument.md) subclass can implement this method to return [`true`](../../Swift/true.md) to enable loading of documents concurrently, using background threads. When this facility is enabled in this way, [`init(contentsOf:ofType:)`](./init%28contentsof,oftype%29.md) executes on a background thread when opening files via the Open panel or from the Finder. This allows concurrent reading of multiple documents and also allows the app to be responsive while reading a large document.

The default implementation of this method returns [`false`](../../Swift/false.md). A subclass override should return [`true`](../../Swift/true.md) only for document types whose reading is thread-safe, as described in [Multicore Considerations](../nsdocument.md#Multicore-Considerations). You should disable undo registration during document reading, which is a good idea even in the absence of concurrency.

If you are checking the current Apple Event for a search string, you should not enable concurrent document opening, because code handling a document opening triggered by an Apple Event cannot get the current Apple Event. This happens because the event is suspended until all documents are read to enable correct reporting of success or error.

## Parameters

- `typeName`: The string that identifies the document type.

## See Also

### Related Documentation
- [class var readableTypes: [String]](./readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
### Reading the Document’s Content
- [func read(from: URL, ofType: String) throws](./read%28from,oftype%29-1vttv.md)
  Sets the contents of this document by reading from a file or file package, of a specified type, located by a URL.
- [func read(from: FileWrapper, ofType: String) throws](./read%28from,oftype%29-3rzsi.md)
  Sets the contents of this document by reading from a file wrapper of a specified type.
- [func read(from: Data, ofType: String) throws](./read%28from,oftype%29-6g6ai.md)
  Sets the contents of this document by reading from data of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/canconcurrentlyreaddocuments(oftype:))*