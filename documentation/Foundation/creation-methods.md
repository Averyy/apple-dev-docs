# Creation methods

**Framework**: Foundation

Create attributed strings from existing content or raw text and apply the initial attributes.

## Topics

### Creating from another string
- [init(string: String)](nsattributedstring/init(string:).md)
  Creates an attributed string with the specified text and no attribute information.
- [init(string: String, attributes: [NSAttributedString.Key : Any]?)](nsattributedstring/init(string:attributes:).md)
  Creates an attributed string with the specified text and attributes.
- [init(attributedString: NSAttributedString)](nsattributedstring/init(attributedstring:).md)
  Creates a new attributed string from the contents of another attributed string.
### Creating a formatted string
- [convenience init(AttributedString)](nsattributedstring/init(_:).md)
  Creates a reference-type attributed string from the specified value-type attributed string.
- [convenience init<S>(AttributedString, including: S.Type) throws](nsattributedstring/init(_:including:)-9gogq.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
- [convenience init<S>(AttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](nsattributedstring/init(_:including:)-8iy4i.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.
### Creating from a data file
- [init(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsattributedstring/init(data:options:documentattributes:).md)
  Creates an attributed string from the contents of the specified data object.
- [init?(docFormat: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(docformat:documentattributes:).md)
  Creates an attributed string from Microsoft Word format data in the specified data object.
- [init(URL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsattributedstring/init(url:options:documentattributes:).md)
  Creates an attributed string from the contents of the specified URL.
### Creating from HTML
- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(html:baseurl:documentattributes:).md)
  Creates an attributed string from the HTML in the specified data object and base URL.
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
### Creating from RTF
- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtf:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [init?(RTFD: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtfd:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.
- [init?(RTFDFileWrapper: FileWrapper, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtfdfilewrapper:documentattributes:).md)
  Creates an attributed string from the specified file wrapper that contains an RTFD document.
### Creating from markdown
- [convenience init(markdown: String, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](nsattributedstring/init(markdown:options:baseurl:)-m9n.md)
  Creates an attributed string from a Markdown-formatted string using the provided options.
- [convenience init(markdown: Data, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](nsattributedstring/init(markdown:options:baseurl:)-5nru2.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [convenience init(contentsOf: URL, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](nsattributedstring/init(contentsof:options:baseurl:).md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.
### Creating a string with an attachment
- [init(attachment: NSTextAttachment)](nsattributedstring/init(attachment:).md)
  Creates an attributed string with an attachment.
- [convenience init(attachment: NSTextAttachment, attributes: [NSAttributedString.Key : Any])](nsattributedstring/init(attachment:attributes:).md)
  Creates an attributed string with an attachment and applies the specified attributes to it.
- [convenience init(adaptiveImageGlyph: NSAdaptiveImageGlyph, attributes: [NSAttributedString.Key : Any])](nsattributedstring/init(adaptiveimageglyph:attributes:).md)
  Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/creation-methods)*