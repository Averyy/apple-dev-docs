# paths

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

An array of bezier paths, in annotation-space coordinates, that compose the annotation.

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
var paths: [UIBezierPath]? { get }
```

*macOS*

```swift
var paths: [NSBezierPath]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, nullable) NSArray<UIBezierPath *> * paths;
```

*macOS*

```objc
@property (nonatomic, readonly, nullable) NSArray<NSBezierPath *> * paths;
```

## See Also

### Configuring Ink Annotations
- [func add(UIBezierPath)](./add%28_%29.md)
  Adds a bezier path to the ink annotation.
- [func remove(UIBezierPath)](./remove%28_%29.md)
  Removes a bezier path from an ink annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/paths)*