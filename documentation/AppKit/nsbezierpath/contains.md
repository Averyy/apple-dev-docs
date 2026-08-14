# contains(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the path contains the specified point.

**Availability**:
- macOS ?+

## Declaration

```swift
func contains(_ point: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the path’s enclosed area contains the specified point; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method checks the point against the path itself and the area it encloses. When determining hits in the enclosed area, this method uses the non-zero winding rule ([`NSNonZeroWindingRule`](nsnonzerowindingrule.md)). It does not take into account the line width used to stroke the path.

## Parameters

- `point`: The point to test against the path, specified in the path object’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/contains(_:))*