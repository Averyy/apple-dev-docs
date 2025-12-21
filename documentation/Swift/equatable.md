# Equatable

**Framework**: Swift  
**Kind**: protocol

A type that can be compared for value equality.

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
protocol Equatable
```

## Mentions

- [Adopting Common Protocols](adopting-common-protocols.md)

#### Overview

Types that conform to the `Equatable` protocol can be compared for equality using the equal-to operator (`==`) or inequality using the not-equal-to operator (`!=`). Most basic types in the Swift standard library conform to `Equatable`.

Some sequence and collection operations can be used more simply when the elements conform to `Equatable`. For example, to check whether an array contains a particular value, you can pass the value itself to the `contains(_:)` method when the array’s element conforms to `Equatable` instead of providing a closure that determines equivalence. The following example shows how the `contains(_:)` method can be used with an array of strings.

```swift
let students = ["Kofi", "Abena", "Efua", "Kweku", "Akosua"]

let nameToCheck = "Kofi"
if students.contains(nameToCheck) {
    print("\(nameToCheck) is signed up!")
} else {
    print("No record of \(nameToCheck).")
}
// Prints "Kofi is signed up!"
```

### Conforming to the Equatable Protocol

Adding `Equatable` conformance to your custom types means that you can use more convenient APIs when searching for particular instances in a collection. `Equatable` is also the base protocol for the `Hashable` and `Comparable` protocols, which allow more uses of your custom type, such as constructing sets or sorting the elements of a collection.

You can rely on automatic synthesis of the `Equatable` protocol’s requirements for a custom type when you declare `Equatable` conformance in the type’s original declaration and your type meets these criteria:

- For a `struct`, all its stored properties must conform to `Equatable`.
- For an `enum`, all its associated values must conform to `Equatable`. (An `enum` without associated values has `Equatable` conformance even without the declaration.)

To customize your type’s `Equatable` conformance, to adopt `Equatable` in a type that doesn’t meet the criteria listed above, or to extend an existing type to conform to `Equatable`, implement the equal-to operator (`==`) as a static method of your type. The standard library provides an implementation for the not-equal-to operator (`!=`) for any `Equatable` type, which calls the custom `==` function and negates its result.

As an example, consider a `StreetAddress` class that holds the parts of a street address: a house or building number, the street name, and an optional unit number. Here’s the initial declaration of the `StreetAddress` type:

```swift
class StreetAddress {
    let number: String
    let street: String
    let unit: String?

    init(_ number: String, _ street: String, unit: String? = nil) {
        self.number = number
        self.street = street
        self.unit = unit
    }
}
```

Now suppose you have an array of addresses that you need to check for a particular address. To use the `contains(_:)` method without including a closure in each call, extend the `StreetAddress` type to conform to `Equatable`.

```swift
extension StreetAddress: Equatable {
    static func == (lhs: StreetAddress, rhs: StreetAddress) -> Bool {
        return
            lhs.number == rhs.number &&
            lhs.street == rhs.street &&
            lhs.unit == rhs.unit
    }
}
```

The `StreetAddress` type now conforms to `Equatable`. You can use `==` to check for equality between any two instances or call the `Equatable`-constrained `contains(_:)` method.

```swift
let addresses = [StreetAddress("1490", "Grove Street"),
                 StreetAddress("2119", "Maple Avenue"),
                 StreetAddress("1400", "16th Street")]
let home = StreetAddress("1400", "16th Street")

print(addresses[0] == home)
// Prints "false"
print(addresses.contains(home))
// Prints "true"
```

Equality implies substitutability—any two instances that compare equally can be used interchangeably in any code that depends on their values. To maintain substitutability, the `==` operator should take into account all visible aspects of an `Equatable` type. Exposing nonvalue aspects of `Equatable` types other than class identity is discouraged, and any that  exposed should be explicitly pointed out in documentation.

Since equality between instances of `Equatable` types is an equivalence relation, any of your custom types that conform to `Equatable` must satisfy three conditions, for any values `a`, `b`, and `c`:

- `a == a` is always `true` (Reflexivity)
- `a == b` implies `b == a` (Symmetry)
- `a == b` and `b == c` implies `a == c` (Transitivity)

Moreover, inequality is the inverse of equality, so any custom implementation of the `!=` operator must guarantee that `a != b` implies `!(a == b)`. The default implementation of the `!=` operator function satisfies this requirement.

#### Equality Is Separate From Identity

The identity of a class instance is not part of an instance’s value. Consider a class called `IntegerRef` that wraps an integer value. Here’s the definition for `IntegerRef` and the `==` function that makes it conform to `Equatable`:

```swift
class IntegerRef: Equatable {
    let value: Int
    init(_ value: Int) {
        self.value = value
    }

    static func == (lhs: IntegerRef, rhs: IntegerRef) -> Bool {
        return lhs.value == rhs.value
    }
}
```

The implementation of the `==` function returns the same value whether its two arguments are the same instance or are two different instances with the same integer stored in their `value` properties. For example:

```swift
let a = IntegerRef(100)
let b = IntegerRef(100)

print(a == a, a == b, separator: ", ")
// Prints "true, true"
```

Class instance identity, on the other hand, is compared using the triple-equals identical-to operator (`===`). For example:

```swift
let c = a
print(c === a, c === b, separator: ", ")
// Prints "true, false"
```

## Topics

### Equatable Requirements
- [static func == (Self, Self) -> Bool](equatable/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](equatable/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Tuple Comparison
- [func == ((), ()) -> Bool](==(_:_:)-958in.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B>((A, B), (A, B)) -> Bool](==(_:_:)-2htbb.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C>((A, B, C), (A, B, C)) -> Bool](==(_:_:)-h88g.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](==(_:_:)-7lhq7.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](==(_:_:)-1hbor.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](==(_:_:)-1ud2a.md)
  Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [func == ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](==(_:_:)-9kf9y.md)
  Returns a Boolean value indicating whether two types are identical.
- [func != ((), ()) -> Bool](!=(_:_:)-18co7.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B>((A, B), (A, B)) -> Bool](!=(_:_:)-7er1l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C>((A, B, C), (A, B, C)) -> Bool](!=(_:_:)-754t2.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D>((A, B, C, D), (A, B, C, D)) -> Bool](!=(_:_:)-7ao4l.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E>((A, B, C, D, E), (A, B, C, D, E)) -> Bool](!=(_:_:)-4fzl6.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != <A, B, C, D, E, F>((A, B, C, D, E, F), (A, B, C, D, E, F)) -> Bool](!=(_:_:)-3nrcc.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [func != ((any (~Copyable & ~Escapable).Type)?, (any (~Copyable & ~Escapable).Type)?) -> Bool](!=(_:_:)-1mxms.md)
  Returns a Boolean value indicating whether two types are not identical.
### Pattern Matching
- [func ~= <T>(T, T) -> Bool](~=(_:_:).md)
  Returns a Boolean value indicating whether two arguments match by value equality.

## Relationships

### Inherited By
- [AdditiveArithmetic](additivearithmetic.md)
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BinaryInteger](binaryinteger.md)
- [Comparable](comparable.md)
- [DistributedActor](../distributed/distributedactor.md)
- [DurationProtocol](durationprotocol.md)
- [FixedWidthInteger](fixedwidthinteger.md)
- [FloatingPoint](floatingpoint.md)
- [Hashable](hashable.md)
- [InstantProtocol](instantprotocol.md)
- [Numeric](numeric.md)
- [OptionSet](optionset.md)
- [SIMD](simd.md)
- [SetAlgebra](setalgebra.md)
- [SignedInteger](signedinteger.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
- [StringProtocol](stringprotocol.md)
- [UnsignedInteger](unsignedinteger.md)
### Conforming Types
- [AnyHashable](anyhashable.md)
- [AnyIndex](anyindex.md)
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
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
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
- [EmptyCollection](emptycollection.md)
- [EnumeratedSequence.Index](enumeratedsequence/index.md)
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
- [JobPriority](jobpriority.md)
- [KeyPath](keypath.md)
- [LazyPrefixWhileSequence.Index](lazyprefixwhilesequence/index.md)
- [LocalTestingActorID](../distributed/localtestingactorid.md)
- [ManagedBufferPointer](managedbufferpointer.md)
- [Mirror.DisplayStyle](mirror/displaystyle-swift.enum.md)
- [Never](never.md)
- [ObjectIdentifier](objectidentifier.md)
- [ObservationRegistrar](../observation/observationregistrar.md)
- [OpaquePointer](opaquepointer.md)
- [Optional](optional.md)
- [Optional.Publisher](optional/publisher-swift.struct.md)
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
- [Result.Publisher](result/publisher-swift.struct.md)
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
- [String.LocalizationValue](string/localizationvalue.md)
- [String.LocalizationValue.Placeholder](string/localizationvalue/placeholder.md)
- [String.StandardComparator](string/standardcomparator.md)
- [Substring](substring.md)
- [SuspendingClock.Instant](suspendingclock/instant.md)
- [Task](task.md)
- [TaskPriority](taskpriority.md)
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
- [UnicodeDecodingResult](unicodedecodingresult.md)
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [UnsafeCurrentTask](unsafecurrenttask.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawPointer](unsaferawpointer.md)
- [WordPair](../synchronization/wordpair.md)
- [WritableKeyPath](writablekeypath.md)

## See Also

- [protocol Comparable](comparable.md)
  A type that can be compared using the relational operators `<`, `<=`, `>=`, and `>`.
- [protocol Identifiable](identifiable.md)
  A class of types whose instances hold the value of an entity with stable identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/equatable)*