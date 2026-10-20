# isSimpleRectangularTextContainer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isSimpleRectangularTextContainer: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSimpleRectangularTextContainer) BOOL simpleRectangularTextContainer;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the text container’s region is a rectangle with no holes or gaps and the edges are parallel to the text view’s coordinate system axes. The default value of this property is [`false`](../../Swift/false.md) when the [`exclusionPaths`](./exclusionpaths.md) property contains one or more items, when the [`maximumNumberOfLines`](./maximumnumberoflines.md) property is not zero, or when you override the [`lineFragmentRect(forProposedRect:at:writingDirection:remaining:)`](./linefragmentrect%28forproposedrect,at,writingdirection,remaining%29.md) method. Otherwise, the default value is [`true`](../../Swift/true.md).

## See Also

### Constraining text layout
- [var maximumNumberOfLines: Int](./maximumnumberoflines.md)
  The maximum number of lines that the text container can store.
- [var lineFragmentPadding: CGFloat](./linefragmentpadding.md)
  The value for the text inset within line fragment rectangles.
- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](./linefragmentrect%28forproposedrect,at,writingdirection,remaining%29.md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/issimplerectangulartextcontainer)*