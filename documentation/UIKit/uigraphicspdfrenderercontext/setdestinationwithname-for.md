# setDestinationWithName(_:for:)

**Framework**: UIKit  
**Kind**: method

Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setDestinationWithName(_ name: String, for rect: CGRect)
```

#### Discussion

Use this method in conjunction with the [`addDestination(withName:at:)`](uigraphicspdfrenderercontext/adddestination(withname:at:).md) method to create internal links within a PDF. This method represents the creation of the links that, when clicked, jump the user to a named destination, created using the [`addDestination(withName:at:)`](uigraphicspdfrenderercontext/adddestination(withname:at:).md) method.

> **Note**:  Specify the `rect` value in the PDF coordinate space, not the Core Graphics coordinate space. This means the origin is in the bottom-left corner of the context rather than the top-left, and the y-axis increases in an upwards direction. Use the [`userSpaceToDeviceSpaceTransform`](https://developer.apple.com/documentation/CoreGraphics/CGContext/userSpaceToDeviceSpaceTransform) property on [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) to map between the two.

For an example of how to use internal links, including mapping between coordinate spaces, see  [`Creating internal links`](uigraphicspdfrenderer#Creating-internal-links.md) in [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md).

## Parameters

- `name`: The name of the destination point to which the PDF viewer jumps.
- `rect`: The region on the current page that becomes the active link area, specified in points in the PDF coordinate space.

## See Also

- [func addDestination(withName: String, at: CGPoint)](uigraphicspdfrenderercontext/adddestination(withname:at:).md)
  Creates a named destination point in the current PDF page.
- [func setURL(URL, for: CGRect)](uigraphicspdfrenderercontext/seturl(_:for:).md)
  Creates a link to an external resource defined by a URL


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/setdestinationwithname(_:for:))*