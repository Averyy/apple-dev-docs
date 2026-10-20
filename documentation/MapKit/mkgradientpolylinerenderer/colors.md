# colors

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An array that represents the gradient’s color transition points.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var colors: [UIColor] { get }
```

*macOS*

```swift
var colors: [NSColor] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<UIColor *> * colors;
```

*macOS*

```objc
@property (nonatomic, copy, readonly) NSArray<NSColor *> * colors;
```

## See Also

### Accessing the gradient colors
- [func setColors([UIColor], locations: [CGFloat])](./setcolors%28_,locations%29-3xrou.md)
  Sets the iOS colors and corresponding unit distance values to create gradients.
- [func setColors([NSColor], locations: [CGFloat])](./setcolors%28_,locations%29-1tuft.md)
  Sets the macOS colors and corresponding unit distance values to create gradients.
- [var locations: [CGFloat]](./locations-7k6qz.md)
  An array of location indexes that correspond to their respective colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/colors)*