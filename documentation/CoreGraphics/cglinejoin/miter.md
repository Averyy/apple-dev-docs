# CGLineJoin.miter

**Framework**: Core Graphics  
**Kind**: case

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case miter
```

#### Discussion

A join with a sharp (angled) corner. Core Graphics draws the outer sides of the lines beyond the endpoint of the path, until they meet. If the length of the miter divided by the line width is greater than the miter limit, a bevel join is used instead. This is the default. To set the miter limit, see [`setMiterLimit(_:)`](cgcontext/setmiterlimit(_:).md).

## See Also

- [CGLineJoin.round](cglinejoin/round.md)
  A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [CGLineJoin.bevel](cglinejoin/bevel.md)
  A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinejoin/miter)*