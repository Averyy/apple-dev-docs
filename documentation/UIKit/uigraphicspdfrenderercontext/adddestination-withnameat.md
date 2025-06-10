# addDestination(withName:at:)

**Framework**: UIKit  
**Kind**: method

Creates a named destination point in the current PDF page.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addDestination(withName name: String, at point: CGPoint)
```

#### Discussion

Use this method in conjunction with the [`setDestinationWithName(_:for:)`](uigraphicspdfrenderercontext/setdestinationwithname(_:for:).md) method to create internal links within a PDF. This method represents the creation of the points to which the PDF viewer will jump when a user clicks a link.

> **Note**:  Specify the `point` value in the PDF coordinate space, not the Core Graphics context coordinate space. This means that the origin is in the bottom-left corner of the context rather than the top-left, and the y-axis increases in an upwards direction. Use the [`userSpaceToDeviceSpaceTransform`](https://developer.apple.com/documentation/CoreGraphics/CGContext/userSpaceToDeviceSpaceTransform) property on [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) to map between the two.

For an example of how to use internal links, including mapping between coordinate spaces, see  [`Creating internal links`](uigraphicspdfrenderer#Creating-internal-links.md) in [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md).

## Parameters

- `name`: The name of the destination, used as a reference by the   method.
- `point`: The location of the destination point, in the PDF coordinate space.

## See Also

- [func setDestinationWithName(String, for: CGRect)](uigraphicspdfrenderercontext/setdestinationwithname(_:for:).md)
  Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
- [func setURL(URL, for: CGRect)](uigraphicspdfrenderercontext/seturl(_:for:).md)
  Creates a link to an external resource defined by a URL


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/adddestination(withname:at:))*