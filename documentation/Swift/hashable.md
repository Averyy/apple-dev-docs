# Hashable

**Framework**: Swift  
**Kind**: protocol

A type that can be hashed into a `Hasher` to produce an integer hash value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol Hashable : Equatable
```

## Mentions

- [Adopting Common Protocols](adopting-common-protocols.md)

#### Overview

You can use any type that conforms to the `Hashable` protocol in a set or as a dictionary key. Many types in the standard library conform to `Hashable`: Strings, integers, floating-point and Boolean values, and even sets are hashable by default. Some other types, such as optionals, arrays and ranges automatically become hashable when their type arguments implement the same.

Your own custom types can be hashable as well. When you define an enumeration without associated values, it gains `Hashable` conformance automatically, and you can add `Hashable` conformance to your other custom types by implementing the `hash(into:)` method. For structs whose stored properties are all `Hashable`, and for enum types that have all-`Hashable` associated values, the compiler is able to provide an implementation of `hash(into:)` automatically.

Hashing a value means feeding its essential components into a hash function, represented by the `Hasher` type. Essential components are those that contribute to the type’s implementation of `Equatable`. Two instances that are equal must feed the same values to `Hasher` in `hash(into:)`, in the same order.

### Conforming to the Hashable Protocol

To use your own custom type in a set or as the key type of a dictionary, add `Hashable` conformance to your type. The `Hashable` protocol inherits from the `Equatable` protocol, so you must also satisfy that protocol’s requirements.

The compiler automatically synthesizes your custom type’s `Hashable` and requirements when you declare `Hashable` conformance in the type’s original declaration and your type meets these criteria:

- For a `struct`, all its stored properties must conform to `Hashable`.
- For an `enum`, all its associated values must conform to `Hashable`. (An `enum` without associated values has `Hashable` conformance even without the declaration.)

To customize your type’s `Hashable` conformance, to adopt `Hashable` in a type that doesn’t meet the criteria listed above, or to extend an existing type to conform to `Hashable`, implement the `hash(into:)` method in your custom type.

In your `hash(into:)` implementation, call `combine(_:)` on the provided `Hasher` instance with the essential components of your type. To ensure that your type meets the semantic requirements of the `Hashable` and `Equatable` protocols, it’s a good idea to also customize your type’s `Equatable` conformance to match.

As an example, consider a `GridPoint` type that describes a location in a grid of buttons. Here’s the initial declaration of the `GridPoint` type:

```swift
/// A point in an x-y coordinate system.
struct GridPoint {
    var x: Int
    var y: Int
}
```

You’d like to create a set of the grid points where a user has already tapped. Because the `GridPoint` type is not hashable yet, it can’t be used in a set. To add `Hashable` conformance, provide an `==` operator function and implement the `hash(into:)` method.

```swift
extension GridPoint: Hashable {
    static func == (lhs: GridPoint, rhs: GridPoint) -> Bool {
        return lhs.x == rhs.x && lhs.y == rhs.y
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(x)
        hasher.combine(y)
    }
}
```

The `hash(into:)` method in this example feeds the grid point’s `x` and `y` properties into the provided hasher. These properties are the same ones used to test for equality in the `==` operator function.

Now that `GridPoint` conforms to the `Hashable` protocol, you can create a set of previously tapped grid points.

```swift
var tappedPoints: Set = [GridPoint(x: 2, y: 3), GridPoint(x: 4, y: 1)]
let nextTap = GridPoint(x: 0, y: 1)
if tappedPoints.contains(nextTap) {
    print("Already tapped at (\(nextTap.x), \(nextTap.y)).")
} else {
    tappedPoints.insert(nextTap)
    print("New tap detected at (\(nextTap.x), \(nextTap.y)).")
}
// Prints "New tap detected at (0, 1).")
```

## Topics

### Providing a Hash Value
- [func hash(into: inout Hasher)](hashable/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Deprecated
- [var hashValue: Int](hashable/hashvalue.md)
  The hash value.

## Relationships

### Inherits From
- [Equatable](equatable.md)
### Inherited By
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BinaryInteger](binaryinteger.md)
- [DistributedActor](../distributed/distributedactor.md)
- [FixedWidthInteger](fixedwidthinteger.md)
- [FloatingPoint](floatingpoint.md)
- [InstantProtocol](instantprotocol.md)
- [SIMD](simd.md)
- [SignedInteger](signedinteger.md)
- [StringProtocol](stringprotocol.md)
- [UnsignedInteger](unsignedinteger.md)
### Conforming Types
- [AnyHashable](anyhashable.md)
- [AnyKeyPath](anykeypath.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [AsyncStream.Continuation](asyncstream/continuation.md)
- [AsyncStream.Continuation.Termination](asyncstream/continuation/termination.md)
- [AsyncThrowingStream.Continuation](asyncthrowingstream/continuation.md)
- [AtomicLoadOrdering](../synchronization/atomicloadordering.md)
- [AtomicStoreOrdering](../synchronization/atomicstoreordering.md)
- [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md)
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)
- [Bool](bool.md)
- [Character](character.md)
- [ClosedRange](closedrange.md)
- [ClosedRange.Index](closedrange/index.md)
- [CodingUserInfoKey](codinguserinfokey.md)
- [CollectionDifference](collectiondifference.md)
- [CollectionDifference.Change](collectiondifference/change.md)
- [CollectionDifference.Index](collectiondifference/index.md)
- [ContiguousArray](contiguousarray.md)
- [ContinuousClock.Instant](continuousclock/instant.md)
- [Dictionary](dictionary.md)
- [Dictionary.Index](dictionary/index.md)
- [DiscontiguousSlice](discontiguousslice.md)
- [DiscontiguousSlice.Index](discontiguousslice/index.md)
- [Double](double.md)
- [Duration](duration.md)
- [Duration.TimeFormatStyle](duration/timeformatstyle.md)
- [Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct.md)
- [Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct.md)
- [Duration.UnitsFormatStyle](duration/unitsformatstyle.md)
- [Duration.UnitsFormatStyle.Attributed](duration/unitsformatstyle/attributed-swift.struct.md)
- [Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](duration/unitsformatstyle/fractionalpartdisplaystrategy.md)
- [Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit.md)
- [Duration.UnitsFormatStyle.UnitWidth](duration/unitsformatstyle/unitwidth-swift.struct.md)
- [Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy.md)
- [ExecuteDistributedTargetError.ErrorCode](../distributed/executedistributedtargeterror/errorcode-swift.enum.md)
- [FlattenSequence.Index](flattensequence/index.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [FloatingPointClassification](floatingpointclassification.md)
- [FloatingPointRoundingRule](floatingpointroundingrule.md)
- [FloatingPointSign](floatingpointsign.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [KeyPath](keypath.md)
- [LazyPrefixWhileSequence.Index](lazyprefixwhilesequence/index.md)
- [LocalTestingActorID](../distributed/localtestingactorid.md)
- [Mirror.DisplayStyle](mirror/displaystyle-swift.enum.md)
- [Never](never.md)
- [ObjectIdentifier](objectidentifier.md)
- [ObservationRegistrar](../observation/observationregistrar.md)
- [OpaquePointer](opaquepointer.md)
- [Optional](optional.md)
- [PartialKeyPath](partialkeypath.md)
- [Range](range.md)
- [RangeSet](rangeset.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [ReferenceWritableKeyPath](referencewritablekeypath.md)
- [RegexRepetitionBehavior](regexrepetitionbehavior.md)
- [RegexSemanticLevel](regexsemanticlevel.md)
- [RegexWordBoundaryKind](regexwordboundarykind.md)
- [RemoteCallTarget](../distributed/remotecalltarget.md)
- [Result](result.md)
- [ReversedCollection.Index](reversedcollection/index.md)
- [SIMD16](simd16.md)
- [SIMD2](simd2.md)
- [SIMD3](simd3.md)
- [SIMD32](simd32.md)
- [SIMD4](simd4.md)
- [SIMD64](simd64.md)
- [SIMD8](simd8.md)
- [SIMDMask](simdmask.md)
- [Set](set.md)
- [Set.Index](set/index.md)
- [String](string.md)
- [String.Comparator](string/comparator.md)
- [String.Encoding](string/encoding.md)
- [String.Index](string/index.md)
- [String.IntentInputOptions.CapitalizationType](string/intentinputoptions/capitalizationtype-swift.enum.md)
- [String.IntentInputOptions.KeyboardType](string/intentinputoptions/keyboardtype-swift.enum.md)
- [String.LocalizationValue.Placeholder](string/localizationvalue/placeholder.md)
- [String.StandardComparator](string/standardcomparator.md)
- [Substring](substring.md)
- [SuspendingClock.Instant](suspendingclock/instant.md)
- [Task](task.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)
- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)
- [Unicode.GeneralCategory](unicode/generalcategory.md)
- [Unicode.NumericType](unicode/numerictype.md)
- [Unicode.Scalar](unicode/scalar.md)
- [Unicode.UTF32](unicode/utf32.md)
- [Unicode.UTF8.ValidationError](unicode/utf8/validationerror.md)
- [Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct.md)
- [UnsafeCurrentTask](unsafecurrenttask.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawPointer](unsaferawpointer.md)
- [WordPair](../synchronization/wordpair.md)
- [WritableKeyPath](writablekeypath.md)

## See Also

- [struct Hasher](hasher.md)
  The universal hash function used by `Set` and `Dictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/hashable)*