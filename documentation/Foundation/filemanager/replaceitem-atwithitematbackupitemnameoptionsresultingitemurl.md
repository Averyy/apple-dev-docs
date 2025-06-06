# replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)

**Framework**: Foundation  
**Kind**: method

Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replaceItem(at originalItemURL: URL, withItemAt newItemURL: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions = [], resultingItemURL resultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws
```

#### Discussion

By default, the creation date, permissions, Finder label and color, and Spotlight comments of the original item are preserved on the new item. You can configure which metadata is preserved using the `options` parameter.

This method works only when the `originalItemURL` and `newItemURL` parameters are located on the same volume. Attempting to call this method by passing `originalItemURL` and `newItemURL` parameters that have locations on different volumes results in an error. Instead, you can call the [`url(for:in:appropriateFor:create:)`](filemanager/url(for:in:appropriatefor:create:).md) method, passing [`FileManager.SearchPathDirectory.itemReplacementDirectory`](filemanager/searchpathdirectory/itemreplacementdirectory.md) as the search path directory, to get a temporary URL on the destination’s volume that is suitable for use with this method.

If an error occurs and the original item is not in the original location or a temporary location, the resulting error object contains a user info dictionary with the key `"NSFileOriginalItemLocationKey"`. The value assigned to that key is an [`NSURL`](nsurl.md) object with the location of the item. The error code is one of the file-related errors described in [`NSError Codes`](1448136-nserror-codes.md).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `originalItemURL`: The item containing the content you want to replace.
- `newItemURL`: The item containing the new content for  . It is recommended that you put this item in a temporary directory as provided by the OS. If a temporary directory is not available, put this item in a uniquely named directory that is in the same directory as the original item.
- `backupItemName`: The backup item will be removed in the event of success unless the   option is provided in  .
- `options`: The options to use during the replacement. Typically, you pass   for this parameter, which uses only the metadata from the new item. You can also combine the options described in   using the C-bitwise OR operator.
- `resultingURL`: On input, a pointer for a URL object. When the item is replaced, this pointer is set to the URL of the new item. If no new file system object is required, the URL object in this parameter may be the same passed to the   parameter. However, if a new file system object is required, the URL object may be different. For example, replacing an RTF document with an RTFD document requires the creation of a new file.

## See Also

- [func replaceItemAt(URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> URL?](filemanager/replaceitemat(_:withitemat:backupitemname:options:)-4210g.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions.md)
  Options for specifying the behavior of file replacement operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:))*