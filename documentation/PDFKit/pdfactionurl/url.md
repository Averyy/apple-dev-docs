# url

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the URL associated with the URL action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * URL;
```

#### Return Value

The URL associated with the action, or `NULL` if no URL is specified.

## See Also

### Related Documentation
- [class PDFActionURL](../pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionurl/url)*