# add(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Adds a bezier path to the ink annotation.

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
func add(_ path: UIBezierPath)
```

*macOS*

```swift
func add(_ path: NSBezierPath)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) addBezierPath:(UIBezierPath *) path;
```

*macOS*

```objc
- (void) addBezierPath:(NSBezierPath *) path;
```

## Parameters

- `path`: The bezier path to add, in annotation-space coordinates.

## See Also

### Configuring Ink Annotations
- [var paths: [UIBezierPath]?](./paths.md)
  An array of bezier paths, in annotation-space coordinates, that compose the annotation.
- [func remove(UIBezierPath)](./remove%28_%29.md)
  Removes a bezier path from an ink annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/add(_:))*