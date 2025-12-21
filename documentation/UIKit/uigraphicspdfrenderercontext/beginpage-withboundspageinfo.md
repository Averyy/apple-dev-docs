# beginPage(withBounds:pageInfo:)

**Framework**: UIKit  
**Kind**: method

Marks the beginning of a new page in the PDF context and configures it using the specified values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func beginPage(withBounds bounds: CGRect, pageInfo: [String : Any])
```

#### Discussion

This function ends any previous page before beginning a new one. It sets the media box of the new page to the value in the [`kCGPDFContextMediaBox`](https://developer.apple.com/documentation/CoreGraphics/kCGPDFContextMediaBox) key of the `pageInfo` dictionary, or to the value in the bounds parameter if the dictionary does not contain the key.

## Parameters

- `bounds`: A rectangle that specifies the size and location of the new PDF page. This rectangle corresponds to the media box in PDF terminology.
- `pageInfo`: A dictionary that specifies additional page-related information, such as the boxes that define different parts of the page. For a list of keys you can include in this dictionary, see   in  .

## See Also

- [func beginPage()](uigraphicspdfrenderercontext/beginpage.md)
  Marks the beginning of a new page in the PDF context and configures it using default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:))*