# Creation methods

**Framework**: Foundation  
**Role**: API Collection

Create attributed strings from existing content or raw text and apply the initial attributes.

## Topics

### Creating from another string
- [init(string: String)](./nsattributedstring/init%28string%29.md)
  Creates an attributed string with the specified text and no attribute information.
- [init(string: String, attributes: [NSAttributedString.Key : Any]?)](./nsattributedstring/init%28string,attributes%29.md)
  Creates an attributed string with the specified text and attributes.
- [init(attributedString: NSAttributedString)](./nsattributedstring/init%28attributedstring%29.md)
  Creates a new attributed string from the contents of another attributed string.
### Creating a formatted string
- [convenience init(AttributedString)](./nsattributedstring/init%28_%29.md)
  Creates a reference-type attributed string from the specified value-type attributed string.
- [convenience init<S>(AttributedString, including: S.Type) throws](./nsattributedstring/init%28_,including%29-9gogq.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
- [convenience init<S>(AttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](./nsattributedstring/init%28_,including%29-8iy4i.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.
### Creating from a data file
- [init(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./nsattributedstring/init%28data,options,documentattributes%29.md)
  Creates an attributed string from the contents of the specified data object.
- [init?(docFormat: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28docformat,documentattributes%29.md)
  Creates an attributed string from Microsoft Word format data in the specified data object.
- [init(URL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./nsattributedstring/init%28url,options,documentattributes%29.md)
  Creates an attributed string from the contents of the specified URL.
### Creating from HTML
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./nsattributedstring/loadfromhtml%28request,options,completionhandler%29.md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./nsattributedstring/loadfromhtml%28fileurl,options,completionhandler%29.md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./nsattributedstring/loadfromhtml%28string,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./nsattributedstring/loadfromhtml%28data,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](./nsattributedstring/completionhandler.md)
  A completion handler for getting an asynchronous attributed string.
- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28html,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28html,baseurl,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28html,options,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object.
### Creating from RTF
- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28rtf,documentattributes%29.md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [init?(RTFD: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28rtfd,documentattributes%29.md)
  Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.
- [init?(RTFDFileWrapper: FileWrapper, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28rtfdfilewrapper,documentattributes%29.md)
  Creates an attributed string from the specified file wrapper that contains an RTFD document.
### Creating from markdown
- [convenience init(markdown: String, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./nsattributedstring/init%28markdown,options,baseurl%29-m9n.md)
  Creates an attributed string from a Markdown-formatted string using the provided options.
- [convenience init(markdown: Data, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./nsattributedstring/init%28markdown,options,baseurl%29-5nru2.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [convenience init(contentsOf: URL, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./nsattributedstring/init%28contentsof,options,baseurl%29.md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.
### Creating a string with an attachment
- [init(attachment: NSTextAttachment)](./nsattributedstring/init%28attachment%29.md)
  Creates an attributed string with an attachment.
- [convenience init(attachment: NSTextAttachment, attributes: [NSAttributedString.Key : Any])](./nsattributedstring/init%28attachment,attributes%29.md)
  Creates an attributed string with an attachment and applies the specified attributes to it.
- [convenience init(adaptiveImageGlyph: NSAdaptiveImageGlyph, attributes: [NSAttributedString.Key : Any])](./nsattributedstring/init%28adaptiveimageglyph,attributes%29.md)
  Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/creation-methods)*