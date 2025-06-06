# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript

Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(idx: Int) -> GKBehavior { get }
```

#### Return Value

The behavior at the specified index.

#### Discussion

The order of individual behaviors in a composite behavior is undefined. However, you can use this method to enumerate all individual behaviors in a composite behavior.

## Parameters

- `idx`: An index in the composite behavior’s list of individual behaviors; it must be less than the value of the   property.

## See Also

- [subscript(GKBehavior) -> NSNumber](gkcompositebehavior/subscript(_:)-6jng9.md)
  Returns the weight associated with the behavior specified by subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/subscript(_:)-6krdg)*