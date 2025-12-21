# init(fileURL:)

**Framework**: UIKit  
**Kind**: init

Returns a document object initialized with its file-system location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(fileURL url: URL)
```

#### Return Value

A `UIDocument` object or `nil` if the object could not be created.

#### Discussion

After you create a document object and no file exists for it yet, you should next call the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) to write the document to its file-system location in the application sandbox. If `url` locates an existing document file, call [`open(completionHandler:)`](uidocument/open(completionhandler:).md) after creating the document object. The second parameter of this method, the save operation constant, should be [`UIDocument.SaveOperation.forCreating`](uidocument/saveoperation/forcreating.md) when there is no document file yet. In the completion handler, if you want the document to be automatically synced with other devices you should ensure that its URL is based in a ubiquitous container; see [`Designing for Documents in iCloud`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForDocumentsIniCloud.html#//apple_ref/doc/uid/TP40012094-CH2-SW1) for more information.

## Parameters

- `url`: A file URL identifying the location in the application sandbox where document data is to be written. Passing in   or an empty URL results in the throwing of an  .

## See Also

- [var fileURL: URL](uidocument/fileurl.md)
  The file URL you use to initialize the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/init(fileurl:))*