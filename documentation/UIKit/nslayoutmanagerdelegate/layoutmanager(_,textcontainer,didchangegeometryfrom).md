# layoutManager(_:textContainer:didChangeGeometryFrom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFrom oldSize: CGSize)
```

```objc
- (void) layoutManager:(NSLayoutManager *) layoutManager textContainer:(NSTextContainer *) textContainer didChangeGeometryFromSize:(CGSize) oldSize;
```

## Discussion

The delegate can react to the geometry change and perform adjustments such as recreating an exclusion path.

## Parameters

- `layoutManager`: The layout manager invalidating layout.
- `textContainer`: The text container that changed geometry.
- `oldSize`: The size of the text container before it changed geometry.

## See Also

### Responding to text container layout
- [func layoutManager(NSLayoutManager, didCompleteLayoutFor: NSTextContainer?, atEnd: Bool)](./layoutmanager%28_,didcompletelayoutfor,atend%29.md)
  Informs the delegate when the layout manager finishes laying out text in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:textcontainer:didchangegeometryfrom:))*