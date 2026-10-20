# init(image:options:)

**Framework**: PDFKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
init?(image: UIImage, options: [PDFPage.ImageInitializationOption : Any] = [:])
```

*macOS*

```swift
init?(image: NSImage, options: [PDFPage.ImageInitializationOption : Any] = [:])
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (instancetype) initWithImage:(UIImage *) image options:(NSDictionary<NSString *,id> *) options;
```

*macOS*

```objc
- (instancetype) initWithImage:(NSImage *) image options:(NSDictionary<NSString *,id> *) options;
```

## See Also

### Initializers
- [init()](./init%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/init(image:options:))*