# init(HTML:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from the HTML in the specified data object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(html data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

#### Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Parameters

- `data`: A data object with text in HTML format. The method uses this data to create the attributed string.
- `options`: Specifies additional options for loading the document. For a list of possible keys, see  .
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify   if you don’t want the document attributes.

## See Also

- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:baseurl:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(request:options:completionhandler:).md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(fileurl:options:completionhandler:).md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(string:options:completionhandler:).md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(data:options:completionhandler:).md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](nsattributedstring/completionhandler.md)
  A completion handler for getting an asynchronous attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(html:options:documentattributes:))*