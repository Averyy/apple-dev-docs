# ManagedMediaListResponse.BooksItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a managed book.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedMediaListResponse.BooksItem
```

## Properties

- `Author` (string): The name of the book’s author.
- `iTunesStoreID` (integer) *(required)*: The book’s iTunes Store identifier.
- `Kind` (string): The kind of the media, which is one of the following values: - `pdf`: A PDF file
- `epub`: An EPUB file in `gzip` format
- `ibooks`: An iBooks Author file in `gzip` format
- The file extension in the URL This value is available in iOS 8 and later.
- `PersistentID` (string): The book’s persistent identifier in reverse-DNS form; for example, `com.acme.manuals.training`.
- `State` (string): The installation state of this book, which is one of the following values: - `Queued`
- `PromptingForLogin`
- `Updating`
- `Installing`
- `Managed`
- `ManagedButUninstalled`
- `Installed`
- `Uninstalled`
- `Failed`
- `Unknown` The `Failed` and `Unknown` states are transient and the device only reports them once. Books from the Book Store report their state as `Installed` instead of `Managed`.
- `Title` (string): The book’s title.
- `Version` (string): The book’s version number.

## See Also

- [object ManagedMediaListResponse.ErrorChainItem](managedmedialistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmedialistresponse/booksitem)*