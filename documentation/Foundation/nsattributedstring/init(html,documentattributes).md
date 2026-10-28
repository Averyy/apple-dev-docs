# init(HTML:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an attributed string from the HTML in the specified data object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(HTML data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```swift
init?(html data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```objc
- (instancetype) initWithHTML:(NSData *) data documentAttributes:(NSDictionary<NSString *,id> **) dict;
```

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Discussion

> **Note**:  Apple discourages the use of this symbol. Use [`loadFromHTML(data:options:completionHandler:)`](./loadfromhtml%28data,options,completionhandler%29.md) instead.

## Parameters

- `data`: A data object with text in HTML format. The method uses this data to create the attributed string.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes

## See Also

### Creating from HTML
- [class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28request,options,completionhandler%29.md)
  Creates an attributed string by converting the contents of the specified HTML URL request.
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28fileurl,options,completionhandler%29.md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28string,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28data,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](./completionhandler.md)
  A completion handler for getting an asynchronous attributed string.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28html,baseurl,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28html,options,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(html:documentattributes:))*