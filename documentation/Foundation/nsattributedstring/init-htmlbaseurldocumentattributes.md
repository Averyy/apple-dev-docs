# init(HTML:baseURL:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from the HTML in the specified data object and base URL.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(html data: Data, baseURL base: URL, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

#### Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Parameters

- `data`: A data object with text in HTML format. The method uses this data to create the attributed string.
- `base`: An   that represents the base URL for all links within the HTML.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify   if you don’t want the document attributes.

## See Also

- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:options:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(request:options:completionhandler:).md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(fileurl:options:completionhandler:).md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(string:options:completionhandler:).md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](nsattributedstring/loadfromhtml(data:options:completionhandler:).md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](nsattributedstring/completionhandler.md)
  A completion handler for getting an asynchronous attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(html:baseurl:documentattributes:))*