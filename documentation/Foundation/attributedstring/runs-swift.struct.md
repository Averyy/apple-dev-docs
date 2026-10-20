# AttributedString.Runs

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [AttributedString.Runs.AttributesSlice1](./runs-swift.struct/attributesslice1.md)
- [AttributedString.Runs.AttributesSlice2](./runs-swift.struct/attributesslice2.md)
- [AttributedString.Runs.AttributesSlice3](./runs-swift.struct/attributesslice3.md)
- [AttributedString.Runs.AttributesSlice4](./runs-swift.struct/attributesslice4.md)
- [AttributedString.Runs.AttributesSlice5](./runs-swift.struct/attributesslice5.md)
- [AttributedString.Runs.Run](./runs-swift.struct/run.md)
### Subscripts
- [subscript<T>(T.Type) -> AttributedString.Runs.AttributesSlice1<T>](./runs-swift.struct/subscript%28_%29-5vfpg.md)
- [subscript<T>(KeyPath<AttributeDynamicLookup, T>) -> AttributedString.Runs.AttributesSlice1<T>](./runs-swift.struct/subscript%28_%29-6aptr.md)
- [subscript(AttributedString.Index) -> AttributedString.Runs.Run](./runs-swift.struct/subscript%28_%29-8hdu9.md)
- [subscript<T, U>(T.Type, U.Type) -> AttributedString.Runs.AttributesSlice2<T, U>](./runs-swift.struct/subscript%28_,_%29-3taux.md)
- [subscript<T, U>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>) -> AttributedString.Runs.AttributesSlice2<T, U>](./runs-swift.struct/subscript%28_,_%29-8nn2m.md)
- [subscript<T, U, V>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>) -> AttributedString.Runs.AttributesSlice3<T, U, V>](./runs-swift.struct/subscript%28_,_,_%29-10o3s.md)
- [subscript<T, U, V>(T.Type, U.Type, V.Type) -> AttributedString.Runs.AttributesSlice3<T, U, V>](./runs-swift.struct/subscript%28_,_,_%29-948ef.md)
- [subscript<T, U, V, W>(T.Type, U.Type, V.Type, W.Type) -> AttributedString.Runs.AttributesSlice4<T, U, V, W>](./runs-swift.struct/subscript%28_,_,_,_%29-7h5tw.md)
- [subscript<T, U, V, W>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>, KeyPath<AttributeDynamicLookup, W>) -> AttributedString.Runs.AttributesSlice4<T, U, V, W>](./runs-swift.struct/subscript%28_,_,_,_%29-sac8.md)
- [subscript<T, U, V, W, X>(KeyPath<AttributeDynamicLookup, T>, KeyPath<AttributeDynamicLookup, U>, KeyPath<AttributeDynamicLookup, V>, KeyPath<AttributeDynamicLookup, W>, KeyPath<AttributeDynamicLookup, X>) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X>](./runs-swift.struct/subscript%28_,_,_,_,_%29-9i87e.md)
- [subscript<T, U, V, W, X>(T.Type, U.Type, V.Type, W.Type, X.Type) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X>](./runs-swift.struct/subscript%28_,_,_,_,_%29-o61e.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Accessing Views into the Attributed String
- [var characters: AttributedString.CharacterView](./characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](./characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](./unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [AttributedString.UnicodeScalarView](./unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [var runs: AttributedString.Runs](./runs-swift.property.md)
  The attributed runs of the attributed string, as a view into the underlying string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct)*