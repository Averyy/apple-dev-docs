# addDestination(withName:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addDestinationWithName:(NSString *) name atPoint:(CGPoint) point;
```

#### Discussion

Use this method in conjunction with the [`setDestinationWithName(_:for:)`](./setdestinationwithname%28_,for%29.md) method to create internal links within a PDF. This method represents the creation of the points to which the PDF viewer will jump when a user clicks a link.

> **Note**:  Specify the `point` value in the PDF coordinate space, not the Core Graphics context coordinate space. This means that the origin is in the bottom-left corner of the context rather than the top-left, and the y-axis increases in an upwards direction. Use the [`userSpaceToDeviceSpaceTransform`](../../CoreGraphics/cgcontext/userspacetodevicespacetransform.md) property on [`CGContext`](../../CoreGraphics/cgcontext.md) to map between the two.

For an example of how to use internal links, including mapping between coordinate spaces, see  [Creating internal links](../uigraphicspdfrenderer.md#Creating-internal-links) in [`UIGraphicsPDFRenderer`](../uigraphicspdfrenderer.md).

## Parameters

- `name`: The name of the destination, used as a reference by the [`setDestinationWithName(_:for:)`](./setdestinationwithname%28_,for%29.md) method.
- `point`: The location of the destination point, in the PDF coordinate space.

## See Also

### Managing destinations
- [func setDestinationWithName(String, for: CGRect)](./setdestinationwithname%28_,for%29.md)
  Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
- [func setURL(URL, for: CGRect)](./seturl%28_,for%29.md)
  Creates a link to an external resource defined by a URL


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/adddestination(withname:at:))*