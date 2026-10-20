# CGLineJoin.round

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case round
```

```c
kCGLineJoinRound
```

## See Also

### Constants
- [CGLineJoin.miter](./miter.md)
- [CGLineJoin.bevel](./bevel.md)
  A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinejoin/round)*