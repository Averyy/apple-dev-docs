# init(textLineRects:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a preview parameters object with information about the text you want to preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(textLineRects: [NSValue])
```

```objc
- (instancetype) initWithTextLineRects:(NSArray<NSValue *> *) textLineRects;
```

#### Return Value

A new preview parameters object for a view containing text.

## Parameters

- `textLineRects`: An array of text line rectangles in the coordinate system of the view being animated. UIKit clips the previewed content using the specified rectangles. Wrap each [`CGRect`](../../CoreFoundation/cgrect.md) in an [`NSValue`](../../Foundation/nsvalue.md) object. If you specify an empty array, UIKit shows the entire view.

## See Also

### Creating preview parameters
- [init()](./init%28%29.md)
  Creates a default set of preview parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/init(textlinerects:))*