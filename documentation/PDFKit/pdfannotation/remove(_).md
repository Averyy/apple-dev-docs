# remove(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Removes a bezier path from an ink annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func remove(_ path: UIBezierPath)
```

*macOS*

```swift
func remove(_ path: NSBezierPath)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) removeBezierPath:(UIBezierPath *) path;
```

*macOS*

```objc
- (void) removeBezierPath:(NSBezierPath *) path;
```

## Parameters

- `path`: The bezier path to remove, in annotation-space coordinates.

## See Also

### Configuring Ink Annotations
- [var paths: [UIBezierPath]?](./paths.md)
  An array of bezier paths, in annotation-space coordinates, that compose the annotation.
- [func add(UIBezierPath)](./add%28_%29.md)
  Adds a bezier path to the ink annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/remove(_:))*