# beginPage()

**Framework**: UIKit  
**Kind**: method

Marks the beginning of a new page in the PDF context and configures it using default values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func beginPage()
```

#### Discussion

This function ends any previous page before beginning a new one. It sets the bounds of the new page to the bounds rectangle you supplied when you created the PDF renderer.

## See Also

- [func beginPage(withBounds: CGRect, pageInfo: [String : Any])](uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:).md)
  Marks the beginning of a new page in the PDF context and configures it using the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/beginpage())*