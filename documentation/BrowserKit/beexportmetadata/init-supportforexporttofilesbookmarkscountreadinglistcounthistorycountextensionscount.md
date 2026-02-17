# init(supportForExportToFiles:bookmarksCount:readingListCount:historyCount:extensionsCount:)

**Framework**: BrowserKit  
**Kind**: init

Initializes export metadata with file support information and data counts.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init(supportForExportToFiles supportExportToFiles: Bool, bookmarksCount: Int, readingListCount: Int, historyCount: Int, extensionsCount: Int)
```

## Parameters

- `supportExportToFiles`: A Boolean value that determines whether the sheet offers the option to export the data to files.
- `bookmarksCount`: The number of bookmarks available for export.
- `readingListCount`: The number of reading list items available for export.
- `historyCount`: The number of history visits available for export.
- `extensionsCount`: The number of extensions available for export.

## See Also

- [init?(coder: NSCoder)](beexportmetadata/init(coder:).md)
  Initializes export metadata from a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportmetadata/init(supportforexporttofiles:bookmarkscount:readinglistcount:historycount:extensionscount:))*