# AttributedString.Runs

**Framework**: Foundation  
**Kind**: struct

An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Runs
```

## Topics

### Structures
- [AttributedString.Runs.AttributesSlice1](attributedstring/runs/attributesslice1.md)
- [AttributedString.Runs.AttributesSlice2](attributedstring/runs/attributesslice2.md)
- [AttributedString.Runs.AttributesSlice3](attributedstring/runs/attributesslice3.md)
- [AttributedString.Runs.AttributesSlice4](attributedstring/runs/attributesslice4.md)
- [AttributedString.Runs.AttributesSlice5](attributedstring/runs/attributesslice5.md)
- [AttributedString.Runs.Run](attributedstring/runs/run.md)
### Subscripts
- [subscript<T>(T.Type) -> AttributedString.Runs.AttributesSlice1<T>](attributedstring/runs/subscript(_:)-5vfpg.md)
- [subscript<T>(KeyPath<AttributeDynamicLookup, T>) -> AttributedString.Runs.AttributesSlice1<T>](attributedstring/runs/subscript(_:)-6aptr.md)
- [subscript(AttributedString.Index) -> AttributedString.Runs.Run](attributedstring/runs/subscript(_:)-8hdu9.md)
- [subscript<T, U>(T.Type, U.Type) -> AttributedString.Runs.AttributesSlice2<T, U>](attributedstring/runs/subscript(_:_:)-3taux.md)
- [subscript<T, U>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>) -> AttributedString.Runs.AttributesSlice2<T, U>](attributedstring/runs/subscript(_:_:)-8nn2m.md)
- [subscript<T, U, V>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>) -> AttributedString.Runs.AttributesSlice3<T, U, V>](attributedstring/runs/subscript(_:_:_:)-10o3s.md)
- [subscript<T, U, V>(T.Type, U.Type, V.Type) -> AttributedString.Runs.AttributesSlice3<T, U, V>](attributedstring/runs/subscript(_:_:_:)-948ef.md)
- [subscript<T, U, V, W>(T.Type, U.Type, V.Type, W.Type) -> AttributedString.Runs.AttributesSlice4<T, U, V, W>](attributedstring/runs/subscript(_:_:_:_:)-7h5tw.md)
- [subscript<T, U, V, W>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>, KeyPath<AttributeDynamicLookup, W>) -> AttributedString.Runs.AttributesSlice4<T, U, V, W>](attributedstring/runs/subscript(_:_:_:_:)-sac8.md)
- [subscript<T, U, V, W, X>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>, KeyPath<AttributeDynamicLookup, W>, KeyPath<AttributeDynamicLookup, X>) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X>](attributedstring/runs/subscript(_:_:_:_:_:)-9i87e.md)
- [subscript<T, U, V, W, X>(T.Type, U.Type, V.Type, W.Type, X.Type) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X>](attributedstring/runs/subscript(_:_:_:_:_:)-o61e.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs)*