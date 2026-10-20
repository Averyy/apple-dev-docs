# cgPath

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

An immutable path representing the elements in the path.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var cgPath: CGPath { get }
```

## See Also

### Getting the path’s characteristics
- [var boundingRect: CGRect](./boundingrect.md)
  A rectangle containing all path segments.
- [func contains(CGPoint, eoFill: Bool) -> Bool](./contains%28_,eofill%29.md)
  Returns true if the path contains a specified point.
- [var currentPoint: CGPoint?](./currentpoint.md)
  Returns the last point in the path, or nil if the path contains no points.
- [var description: String](./description.md)
  A description of the path that may be used to recreate the path via `init?(_:)`.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value indicating whether the path contains zero elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/cgpath)*