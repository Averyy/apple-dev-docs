# contents

**Framework**: Core Animation  
**Kind**: property

An object that provides the contents of the layer. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contents: Any? { get set }
```

#### Discussion

A layer can set this property to a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) to display the image as its contents.

The default value of this property is `nil`.

## See Also

- [var contentsRect: CGRect](caemittercell/contentsrect.md)
  A rectangle (in the unit coordinate space) that specifies the portion of [`contents`](caemittercell/contents.md) that the receiver should draw. Animatable.
- [var emitterCells: [CAEmitterCell]?](caemittercell/emittercells.md)
  An optional array containing the sub-cells of this cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/contents)*