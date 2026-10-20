# NSStringFromGCPoint2(_:)

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Returns a string representation of a point.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func NSStringFromGCPoint2(_ point: GCPoint2) -> String
```

```c
extern NSString *NSStringFromGCPoint2(GCPoint2 point);
```

#### Return Value

A string of the form `{a, b}`, where `a` and `b` are the x and y coordinates of `point`.

## Parameters

- `point`: The point to convert to a string.

## See Also

### Comparing and converting points
- [func GCPoint2Equal(GCPoint2, GCPoint2) -> Bool](./gcpoint2equal%28_,_%29.md)
  Returns whether two points are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/nsstringfromgcpoint2(_:))*