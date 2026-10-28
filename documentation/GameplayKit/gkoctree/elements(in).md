# elements(in:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns all objects whose corresponding locations overlap the specified volume.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func elements(in box: GKBox) -> [ElementType]
```

```objc
- (NSArray<NSObject *> *) elementsInBox:(GKBox) box;
```

## Return Value

An array of all matching elements, or an empty array if no objects are found.

## Discussion

You specify the point or region corresponding to an object when you add it to the tree with the [`add(_:at:)`](./add%28_,at%29.md) or [`add(_:in:)`](./add%28_,in%29.md) method. This method follows the same path down the tree as the two `addElement` methods, but instead of adding a new object to the tree, returns the list of all objects stored in the tree node corresponding to the specified point.

## See Also

### Searching for Elements
- [func elements(at: vector_float3) -> [ElementType]](./elements%28at%29.md)
  Returns all objects whose corresponding locations overlap the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkoctree/elements(in:))*