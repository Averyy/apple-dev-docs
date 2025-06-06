# NSAttributedString.CompletionHandler

**Framework**: Foundation  
**Kind**: typealias

A completion handler for getting an asynchronous attributed string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionHandler = (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void
```

## Parameters

- `attributedString`: The attributed string, or nil if the method couldn’t create the string.
- `attributes`: A dictionary containing document-level attributes. This parameter is   if the document doesn’t have any attributes.
- `error`: An error object if an error occurred, or   if the method returned the string successfully.

## See Also

- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:baseurl:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:options:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(request:options:completionhandler:).md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(fileurl:options:completionhandler:).md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(string:options:completionhandler:).md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: NSAttributedString.CompletionHandler)](nsattributedstring/loadfromhtml(data:options:completionhandler:).md)
  Creates an attributed string from the specified HTML data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/completionhandler)*