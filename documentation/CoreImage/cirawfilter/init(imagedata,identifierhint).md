# init(imageData:identifierHint:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a RAW filter from the image data and type hint that you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(imageData data: Data, identifierHint: String?)
```

```objc
+ (instancetype) filterWithImageData:(NSData *) data identifierHint:(NSString *) identifierHint;
```

## Parameters

- `data`: The image data.
- `identifierHint`: A string that identifies the image type.

## See Also

### Creating a filter
- [convenience init?(cvPixelBuffer: CVPixelBuffer, properties: [AnyHashable : Any])](./init%28cvpixelbuffer,properties%29-6209q.md)
  Creates a RAW filter from the pixel buffer and its properties that you specify.
- [convenience init?(imageURL: URL)](./init%28imageurl%29.md)
  Creates a RAW filter from the image at the URL location that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/init(imagedata:identifierhint:))*