# animation(_:value:)

**Framework**: FamilyControls  
**Kind**: method

Applies the given animation to this view when the specified value changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

#### Return Value

A view that applies `animation` to this view whenever `value` changes.

## Parameters

- `animation`: The animation to apply. If   is  , the view   doesn’t animate.
- `value`: A value to monitor for changes.

## See Also

- [func transaction((inout Transaction) -> Void) -> some View](familyactivitypicker/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](familyactivitypicker/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/animation(_:value:))*