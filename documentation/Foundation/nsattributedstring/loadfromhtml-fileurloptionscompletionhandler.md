# loadFromHTML(fileURL:options:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates an attributed string by converting the content of a local HTML file at the specified URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func fromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:]) async throws -> (NSAttributedString, [NSAttributedString.DocumentAttributeKey : Any])
```

## Parameters

- `fileURL`: A URL that specifies the file to load.
- `options`: Specifies additional options for loading the document. For a list of possible keys, see  .
- `completionHandler`: A completion handler to execute with the results.

## See Also

- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:baseurl:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:options:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(request:options:completionhandler:).md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(string:options:completionhandler:).md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(data:options:completionhandler:).md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](nsattributedstring/completionhandler.md)
  A completion handler for getting an asynchronous attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/loadfromhtml(fileurl:options:completionhandler:))*