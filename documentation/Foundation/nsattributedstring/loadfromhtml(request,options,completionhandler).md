# loadFromHTML(request:options:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an attributed string by converting the contents of the specified HTML URL request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func loadFromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], completionHandler: @escaping @Sendable (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)
```

```swift
class func fromHTML(request: URLRequest, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:]) async throws -> (NSAttributedString, [NSAttributedString.DocumentAttributeKey : Any])
```

```objc
+ (void) loadFromHTMLWithRequest:(NSURLRequest *) request options:(NSDictionary<NSString *,id> *) options completionHandler:(NSAttributedStringCompletionHandler) completionHandler;
```

## Parameters

- `request`: A request to fetch an HTML document.
- `options`: Specifies additional options for loading the document. For a list of possible keys, see [`NSAttributedStringDocumentReadingOptionKey`](../../UIKit/nsattributedstringdocumentreadingoptionkey.md).
- `completionHandler`: A completion handler to execute with the results.

## See Also

### Creating from HTML
- [class func loadFromHTML(fileURL: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28fileurl,options,completionhandler%29.md)
  Creates an attributed string by converting the content of a local HTML file at the specified URL.
- [class func loadFromHTML(string: String, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28string,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML string.
- [class func loadFromHTML(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], completionHandler: (NSAttributedString?, [NSAttributedString.DocumentAttributeKey : Any]?, (any Error)?) -> Void)](./loadfromhtml%28data,options,completionhandler%29.md)
  Creates an attributed string from the specified HTML data.
- [NSAttributedString.CompletionHandler](./completionhandler.md)
  A completion handler for getting an asynchronous attributed string.
- [init?(HTML: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28html,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object.
- [init?(HTML: Data, baseURL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28html,baseurl,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object and base URL.
- [init?(HTML: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28html,options,documentattributes%29.md)
  Creates an attributed string from the HTML in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/loadfromhtml(request:options:completionhandler:))*