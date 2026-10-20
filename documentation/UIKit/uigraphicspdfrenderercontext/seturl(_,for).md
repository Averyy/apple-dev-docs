# setURL(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a link to an external resource defined by a URL

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setURL(_ url: URL, for rect: CGRect)
```

```objc
- (void) setURL:(NSURL *) url forRect:(CGRect) rect;
```

#### Discussion

Use this method to create links to external resources in the current page of a PDF. The URL is interpreted by the PDF viewer.

> **Note**:  Specify the `rect` value in the PDF coordinate space, not the Core Graphics context coordinate space. This means that the origin is in the bottom-left rather than the top-left, and the y-axis increases in an upwards direction. Use the [`userSpaceToDeviceSpaceTransform`](../../CoreGraphics/cgcontext/userspacetodevicespacetransform.md) property on [`CGContext`](../../CoreGraphics/cgcontext.md) to map between the two.

To create internal links within the current PDF document, use [`addDestination(withName:at:)`](./adddestination%28withname,at%29.md) and [`setDestinationWithName(_:for:)`](./setdestinationwithname%28_,for%29.md).

## Parameters

- `url`: The external URL that the user is directed to on clicking the link.
- `rect`: The region of the current page that becomes the active link area, specified in points in the PDF coordinate space.

## See Also

### Managing destinations
- [func addDestination(withName: String, at: CGPoint)](./adddestination%28withname,at%29.md)
  Creates a named destination point in the current PDF page.
- [func setDestinationWithName(String, for: CGRect)](./setdestinationwithname%28_,for%29.md)
  Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/seturl(_:for:))*