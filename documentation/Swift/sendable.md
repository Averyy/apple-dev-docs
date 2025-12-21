# Sendable

**Framework**: Swift  
**Kind**: protocol

A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.

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
protocol Sendable : SendableMetatype
```

#### Overview

Values of the type may have no shared mutable state, or they may protect that state with a lock or by forcing it to only be accessed from a specific actor.

You can safely pass values of a sendable type from one concurrency domain to another — for example, you can pass a sendable value as the argument when calling an actor’s methods. All of the following can be marked as sendable:

- Value types
- Reference types with no mutable storage
- Reference types that internally manage access to their state
- Functions and closures (by marking them with `@Sendable`)

Although this protocol doesn’t have any required methods or properties, it does have semantic requirements that are enforced at compile time. These requirements are listed in the sections below. Conformance to `Sendable` must be declared in the same file as the type’s declaration.

To declare conformance to `Sendable` without any compiler enforcement, write `@unchecked Sendable`. You are responsible for the correctness of unchecked sendable types, for example, by protecting all access to its state with a lock or a queue. Unchecked conformance to `Sendable` also disables enforcement of the rule that conformance must be in the same file.

For information about the language-level concurrency model that `Task` is part of, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

##### Sendable Structures and Enumerations

To satisfy the requirements of the `Sendable` protocol, an enumeration or structure must have only sendable members and associated values. In some cases, structures and enumerations that satisfy the requirements implicitly conform to `Sendable`:

- Frozen structures and enumerations
- Structures and enumerations that aren’t public and aren’t marked `@usableFromInline`.

Otherwise, you need to declare conformance to `Sendable` explicitly.

Structures that have nonsendable stored properties and enumerations that have nonsendable associated values can be marked as `@unchecked Sendable`, disabling compile-time correctness checks, after you manually verify that they satisfy the `Sendable` protocol’s semantic requirements.

##### Sendable Actors

All actor types implicitly conform to `Sendable` because actors ensure that all access to their mutable state is performed sequentially.

##### Sendable Classes

To satisfy the requirements of the `Sendable` protocol, a class must:

- Be marked `final`
- Contain only stored properties that are immutable and sendable
- Have no superclass or have `NSObject` as the superclass

Classes marked with `@MainActor` are implicitly sendable, because the main actor coordinates all access to its state. These classes can have stored properties that are mutable and nonsendable.

Classes that don’t meet the requirements above can be marked as `@unchecked Sendable`, disabling compile-time correctness checks, after you manually verify that they satisfy the `Sendable` protocol’s semantic requirements.

##### Sendable Functions and Closures

Instead of conforming to the `Sendable` protocol, you mark sendable functions and closures with the `@Sendable` attribute. Any values that the function or closure captures must be sendable. In addition, sendable closures must use only by-value captures, and the captured values must be of a sendable type.

In a context that expects a sendable closure, a closure that satisfies the requirements implicitly conforms to `Sendable` — for example, in a call to `Task.detached(priority:operation:)`.

You can explicitly mark a closure as sendable by writing `@Sendable` as part of a type annotation, or by writing `@Sendable` before the closure’s parameters — for example:

```swift
let sendableClosure = { @Sendable (number: Int) -> String in
    if number > 12 {
        return "More than a dozen."
    } else {
        return "Less than a dozen"
    }
}
```

##### Sendable Tuples

To satisfy the requirements of the `Sendable` protocol, all of the elements of the tuple must be sendable. Tuples that satisfy the requirements implicitly conform to `Sendable`.

##### Sendable Metatypes

Metatypes such as `Int.Type` implicitly conform to the `Sendable` protocol.

## Relationships

### Inherits From
- [SendableMetatype](sendablemetatype.md)
### Inherited By
- [Actor](actor.md)
- [Clock](clock.md)
- [CodingKey](codingkey.md)
- [DistributedActor](../distributed/distributedactor.md)
- [DistributedActorSystem](../distributed/distributedactorsystem.md)
- [DistributedActorSystemError](../distributed/distributedactorsystemerror.md)
- [DurationProtocol](durationprotocol.md)
- [Error](error.md)
- [Executor](executor.md)
- [InstantProtocol](instantprotocol.md)
- [SerialExecutor](serialexecutor.md)
- [TaskExecutor](taskexecutor.md)
- [UnsafeSendable](unsafesendable.md)
### Conforming Types
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [AsyncCompactMapSequence](asynccompactmapsequence.md)
- [AsyncCompactMapSequence.Iterator](asynccompactmapsequence/iterator.md)
- [AsyncDropFirstSequence](asyncdropfirstsequence.md)
- [AsyncDropFirstSequence.Iterator](asyncdropfirstsequence/iterator.md)
- [AsyncDropWhileSequence](asyncdropwhilesequence.md)
- [AsyncDropWhileSequence.Iterator](asyncdropwhilesequence/iterator.md)
- [AsyncFilterSequence](asyncfiltersequence.md)
- [AsyncFilterSequence.Iterator](asyncfiltersequence/iterator.md)
- [AsyncFlatMapSequence](asyncflatmapsequence.md)
- [AsyncFlatMapSequence.Iterator](asyncflatmapsequence/iterator.md)
- [AsyncMapSequence](asyncmapsequence.md)
- [AsyncMapSequence.Iterator](asyncmapsequence/iterator.md)
- [AsyncPrefixSequence](asyncprefixsequence.md)
- [AsyncPrefixSequence.Iterator](asyncprefixsequence/iterator.md)
- [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
- [AsyncPrefixWhileSequence.Iterator](asyncprefixwhilesequence/iterator.md)
- [AsyncStream](asyncstream.md)
- [AsyncStream.Continuation](asyncstream/continuation.md)
- [AsyncStream.Continuation.BufferingPolicy](asyncstream/continuation/bufferingpolicy.md)
- [AsyncStream.Continuation.Termination](asyncstream/continuation/termination.md)
- [AsyncStream.Continuation.YieldResult](asyncstream/continuation/yieldresult.md)
- [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
- [AsyncThrowingCompactMapSequence.Iterator](asyncthrowingcompactmapsequence/iterator.md)
- [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
- [AsyncThrowingDropWhileSequence.Iterator](asyncthrowingdropwhilesequence/iterator.md)
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
- [AsyncThrowingFilterSequence.Iterator](asyncthrowingfiltersequence/iterator.md)
- [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
- [AsyncThrowingFlatMapSequence.Iterator](asyncthrowingflatmapsequence/iterator.md)
- [AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
- [AsyncThrowingMapSequence.Iterator](asyncthrowingmapsequence/iterator.md)
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
- [AsyncThrowingPrefixWhileSequence.Iterator](asyncthrowingprefixwhilesequence/iterator.md)
- [AsyncThrowingStream](asyncthrowingstream.md)
- [AsyncThrowingStream.Continuation](asyncthrowingstream/continuation.md)
- [AsyncThrowingStream.Continuation.BufferingPolicy](asyncthrowingstream/continuation/bufferingpolicy.md)
- [AsyncThrowingStream.Continuation.Termination](asyncthrowingstream/continuation/termination.md)
- [AsyncThrowingStream.Continuation.YieldResult](asyncthrowingstream/continuation/yieldresult.md)
- [Atomic](../synchronization/atomic.md)
- [AtomicLazyReference](../synchronization/atomiclazyreference.md)
- [AtomicLoadOrdering](../synchronization/atomicloadordering.md)
- [AtomicStoreOrdering](../synchronization/atomicstoreordering.md)
- [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md)
- [Bool](bool.md)
- [CancellationError](cancellationerror.md)
- [Character](character.md)
- [CheckedContinuation](checkedcontinuation.md)
- [ClosedRange](closedrange.md)
- [ClosedRange.Index](closedrange/index.md)
- [CodingUserInfoKey](codinguserinfokey.md)
- [CollectionDifference](collectiondifference.md)
- [CollectionDifference.Change](collectiondifference/change.md)
- [CollectionDifference.Index](collectiondifference/index.md)
- [CollectionOfOne](collectionofone.md)
- [CollectionOfOne.Iterator](collectionofone/iterator.md)
- [CommandLine](commandline.md)
- [ContiguousArray](contiguousarray.md)
- [ContinuousClock](continuousclock.md)
- [ContinuousClock.Instant](continuousclock/instant.md)
- [DecodingError](decodingerror.md)
- [DecodingError.Context](decodingerror/context.md)
- [DefaultIndices](defaultindices.md)
- [DefaultStringInterpolation](defaultstringinterpolation.md)
- [Dictionary](dictionary.md)
- [Dictionary.Index](dictionary/index.md)
- [Dictionary.Iterator](dictionary/iterator.md)
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
- [Dictionary.Keys.Iterator](dictionary/keys-swift.struct/iterator.md)
- [Dictionary.Values](dictionary/values-swift.struct.md)
- [Dictionary.Values.Iterator](dictionary/values-swift.struct/iterator.md)
- [DiscontiguousSlice](discontiguousslice.md)
- [DiscontiguousSlice.Index](discontiguousslice/index.md)
- [DistributedActorCodingError](../distributed/distributedactorcodingerror.md)
- [Double](double.md)
- [Double.SIMD16Storage](double/simd16storage.md)
- [Double.SIMD2Storage](double/simd2storage.md)
- [Double.SIMD32Storage](double/simd32storage.md)
- [Double.SIMD4Storage](double/simd4storage.md)
- [Double.SIMD64Storage](double/simd64storage.md)
- [Double.SIMD8Storage](double/simd8storage.md)
- [DropFirstSequence](dropfirstsequence.md)
- [DropWhileSequence](dropwhilesequence.md)
- [DropWhileSequence.Iterator](dropwhilesequence/iterator.md)
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
- [EmptyCollection.Iterator](emptycollection/iterator.md)
- [EncodingError](encodingerror.md)
- [EncodingError.Context](encodingerror/context.md)
- [EnumeratedSequence](enumeratedsequence.md)
- [EnumeratedSequence.Iterator](enumeratedsequence/iterator.md)
- [ExecuteDistributedTargetError](../distributed/executedistributedtargeterror.md)
- [ExecutorJob](executorjob.md)
- [ExecutorJob.Kind](executorjob/kind-swift.struct.md)
- [FlattenSequence](flattensequence.md)
- [FlattenSequence.Index](flattensequence/index.md)
- [FlattenSequence.Iterator](flattensequence/iterator.md)
- [Float](float.md)
- [Float.SIMD16Storage](float/simd16storage.md)
- [Float.SIMD2Storage](float/simd2storage.md)
- [Float.SIMD32Storage](float/simd32storage.md)
- [Float.SIMD4Storage](float/simd4storage.md)
- [Float.SIMD64Storage](float/simd64storage.md)
- [Float.SIMD8Storage](float/simd8storage.md)
- [Float16](float16.md)
- [Float16.SIMD16Storage](float16/simd16storage.md)
- [Float16.SIMD2Storage](float16/simd2storage.md)
- [Float16.SIMD32Storage](float16/simd32storage.md)
- [Float16.SIMD4Storage](float16/simd4storage.md)
- [Float16.SIMD64Storage](float16/simd64storage.md)
- [Float16.SIMD8Storage](float16/simd8storage.md)
- [Float80](float80.md)
- [FloatingPointClassification](floatingpointclassification.md)
- [FloatingPointRoundingRule](floatingpointroundingrule.md)
- [FloatingPointSign](floatingpointsign.md)
- [Hasher](hasher.md)
- [IndexingIterator](indexingiterator.md)
- [InlineArray](inlinearray.md)
- [Int](int.md)
- [Int.SIMD16Storage](int/simd16storage.md)
- [Int.SIMD2Storage](int/simd2storage.md)
- [Int.SIMD32Storage](int/simd32storage.md)
- [Int.SIMD4Storage](int/simd4storage.md)
- [Int.SIMD64Storage](int/simd64storage.md)
- [Int.SIMD8Storage](int/simd8storage.md)
- [Int.Words](int/words-swift.struct.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int16.SIMD16Storage](int16/simd16storage.md)
- [Int16.SIMD2Storage](int16/simd2storage.md)
- [Int16.SIMD32Storage](int16/simd32storage.md)
- [Int16.SIMD4Storage](int16/simd4storage.md)
- [Int16.SIMD64Storage](int16/simd64storage.md)
- [Int16.SIMD8Storage](int16/simd8storage.md)
- [Int16.Words](int16/words-swift.struct.md)
- [Int32](int32.md)
- [Int32.SIMD16Storage](int32/simd16storage.md)
- [Int32.SIMD2Storage](int32/simd2storage.md)
- [Int32.SIMD32Storage](int32/simd32storage.md)
- [Int32.SIMD4Storage](int32/simd4storage.md)
- [Int32.SIMD64Storage](int32/simd64storage.md)
- [Int32.SIMD8Storage](int32/simd8storage.md)
- [Int32.Words](int32/words-swift.struct.md)
- [Int64](int64.md)
- [Int64.SIMD16Storage](int64/simd16storage.md)
- [Int64.SIMD2Storage](int64/simd2storage.md)
- [Int64.SIMD32Storage](int64/simd32storage.md)
- [Int64.SIMD4Storage](int64/simd4storage.md)
- [Int64.SIMD64Storage](int64/simd64storage.md)
- [Int64.SIMD8Storage](int64/simd8storage.md)
- [Int64.Words](int64/words-swift.struct.md)
- [Int8](int8.md)
- [Int8.SIMD16Storage](int8/simd16storage.md)
- [Int8.SIMD2Storage](int8/simd2storage.md)
- [Int8.SIMD32Storage](int8/simd32storage.md)
- [Int8.SIMD4Storage](int8/simd4storage.md)
- [Int8.SIMD64Storage](int8/simd64storage.md)
- [Int8.SIMD8Storage](int8/simd8storage.md)
- [Int8.Words](int8/words-swift.struct.md)
- [IteratorSequence](iteratorsequence.md)
- [Job](job.md)
- [JobPriority](jobpriority.md)
- [JoinedSequence](joinedsequence.md)
- [JoinedSequence.Iterator](joinedsequence/iterator.md)
- [KeyValuePairs](keyvaluepairs.md)
- [LazyPrefixWhileSequence.Index](lazyprefixwhilesequence/index.md)
- [LazySequence](lazysequence.md)
- [LocalTestingActorID](../distributed/localtestingactorid.md)
- [LocalTestingDistributedActorSystem](../distributed/localtestingdistributedactorsystem.md)
- [LocalTestingDistributedActorSystemError](../distributed/localtestingdistributedactorsystemerror.md)
- [MainActor](mainactor.md)
- [MemoryLayout](memorylayout.md)
- [Mirror.DisplayStyle](mirror/displaystyle-swift.enum.md)
- [MutableRawSpan](mutablerawspan.md)
- [MutableSpan](mutablespan.md)
- [Mutex](../synchronization/mutex.md)
- [Never](never.md)
- [ObjectIdentifier](objectidentifier.md)
- [ObservationRegistrar](../observation/observationregistrar.md)
- [Observations](../observation/observations.md)
- [Observations.Iteration](../observation/observations/iteration.md)
- [Optional](optional.md)
- [OutputRawSpan](outputrawspan.md)
- [OutputSpan](outputspan.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeFrom.Iterator](partialrangefrom/iterator.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [PrefixSequence](prefixsequence.md)
- [PrefixSequence.Iterator](prefixsequence/iterator.md)
- [Range](range.md)
- [RangeSet](rangeset.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [RawSpan](rawspan.md)
- [Repeated](repeated.md)
- [Result](result.md)
- [ReversedCollection](reversedcollection.md)
- [ReversedCollection.Index](reversedcollection/index.md)
- [ReversedCollection.Iterator](reversedcollection/iterator.md)
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
- [Set.Iterator](set/iterator.md)
- [Slice](slice.md)
- [Span](span.md)
- [StaticBigInt](staticbigint.md)
- [StaticString](staticstring.md)
- [StrideThrough](stridethrough.md)
- [StrideThroughIterator](stridethroughiterator.md)
- [StrideTo](strideto.md)
- [StrideToIterator](stridetoiterator.md)
- [String](string.md)
- [String.Comparator](string/comparator.md)
- [String.Encoding](string/encoding.md)
- [String.Index](string/index.md)
- [String.Iterator](string/iterator.md)
- [String.LocalizationValue](string/localizationvalue.md)
- [String.LocalizationValue.Placeholder](string/localizationvalue/placeholder.md)
- [String.StandardComparator](string/standardcomparator.md)
- [String.UTF16View](string/utf16view.md)
- [String.UTF16View.Iterator](string/utf16view/iterator.md)
- [String.UTF8View](string/utf8view.md)
- [String.UnicodeScalarView](string/unicodescalarview.md)
- [String.UnicodeScalarView.Iterator](string/unicodescalarview/iterator.md)
- [Substring](substring.md)
- [Substring.UTF16View](substring/utf16view.md)
- [Substring.UTF8View](substring/utf8view.md)
- [Substring.UnicodeScalarView](substring/unicodescalarview.md)
- [SuspendingClock](suspendingclock.md)
- [SuspendingClock.Instant](suspendingclock/instant.md)
- [SystemRandomNumberGenerator](systemrandomnumbergenerator.md)
- [Task](task.md)
- [TaskLocal](tasklocal.md)
- [TaskPriority](taskpriority.md)
- [UInt](uint.md)
- [UInt.SIMD16Storage](uint/simd16storage.md)
- [UInt.SIMD2Storage](uint/simd2storage.md)
- [UInt.SIMD32Storage](uint/simd32storage.md)
- [UInt.SIMD4Storage](uint/simd4storage.md)
- [UInt.SIMD64Storage](uint/simd64storage.md)
- [UInt.SIMD8Storage](uint/simd8storage.md)
- [UInt.Words](uint/words-swift.struct.md)
- [UInt128](uint128.md)
- [UInt128.Words](uint128/words-swift.struct.md)
- [UInt16](uint16.md)
- [UInt16.SIMD16Storage](uint16/simd16storage.md)
- [UInt16.SIMD2Storage](uint16/simd2storage.md)
- [UInt16.SIMD32Storage](uint16/simd32storage.md)
- [UInt16.SIMD4Storage](uint16/simd4storage.md)
- [UInt16.SIMD64Storage](uint16/simd64storage.md)
- [UInt16.SIMD8Storage](uint16/simd8storage.md)
- [UInt16.Words](uint16/words-swift.struct.md)
- [UInt32](uint32.md)
- [UInt32.SIMD16Storage](uint32/simd16storage.md)
- [UInt32.SIMD2Storage](uint32/simd2storage.md)
- [UInt32.SIMD32Storage](uint32/simd32storage.md)
- [UInt32.SIMD4Storage](uint32/simd4storage.md)
- [UInt32.SIMD64Storage](uint32/simd64storage.md)
- [UInt32.SIMD8Storage](uint32/simd8storage.md)
- [UInt32.Words](uint32/words-swift.struct.md)
- [UInt64](uint64.md)
- [UInt64.SIMD16Storage](uint64/simd16storage.md)
- [UInt64.SIMD2Storage](uint64/simd2storage.md)
- [UInt64.SIMD32Storage](uint64/simd32storage.md)
- [UInt64.SIMD4Storage](uint64/simd4storage.md)
- [UInt64.SIMD64Storage](uint64/simd64storage.md)
- [UInt64.SIMD8Storage](uint64/simd8storage.md)
- [UInt64.Words](uint64/words-swift.struct.md)
- [UInt8](uint8.md)
- [UInt8.SIMD16Storage](uint8/simd16storage.md)
- [UInt8.SIMD2Storage](uint8/simd2storage.md)
- [UInt8.SIMD32Storage](uint8/simd32storage.md)
- [UInt8.SIMD4Storage](uint8/simd4storage.md)
- [UInt8.SIMD64Storage](uint8/simd64storage.md)
- [UInt8.SIMD8Storage](uint8/simd8storage.md)
- [UInt8.Words](uint8/words-swift.struct.md)
- [UnboundedRange_](unboundedrange_.md)
- [UnfoldSequence](unfoldsequence.md)
- [Unicode](unicode.md)
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.ASCII.Parser](unicode/ascii/parser.md)
- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)
- [Unicode.GeneralCategory](unicode/generalcategory.md)
- [Unicode.NumericType](unicode/numerictype.md)
- [Unicode.ParseResult](unicode/parseresult.md)
- [Unicode.Scalar](unicode/scalar.md)
- [Unicode.Scalar.Properties](unicode/scalar/properties-swift.struct.md)
- [Unicode.Scalar.UTF16View](unicode/scalar/utf16view.md)
- [Unicode.Scalar.UTF8View](unicode/scalar/utf8view.md)
- [Unicode.UTF16](unicode/utf16.md)
- [Unicode.UTF16.ForwardParser](unicode/utf16/forwardparser.md)
- [Unicode.UTF16.ReverseParser](unicode/utf16/reverseparser.md)
- [Unicode.UTF32](unicode/utf32.md)
- [Unicode.UTF32.Parser](unicode/utf32/parser.md)
- [Unicode.UTF8](unicode/utf8.md)
- [Unicode.UTF8.ForwardParser](unicode/utf8/forwardparser.md)
- [Unicode.UTF8.ReverseParser](unicode/utf8/reverseparser.md)
- [Unicode.UTF8.ValidationError](unicode/utf8/validationerror.md)
- [Unicode.UTF8.ValidationError.Kind](unicode/utf8/validationerror/kind-swift.struct.md)
- [UnicodeDecodingResult](unicodedecodingresult.md)
- [Unmanaged](unmanaged.md)
- [UnownedJob](unownedjob.md)
- [UnownedSerialExecutor](unownedserialexecutor.md)
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [UnsafeContinuation](unsafecontinuation.md)
- [WordPair](../synchronization/wordpair.md)
- [Zip2Sequence](zip2sequence.md)
- [Zip2Sequence.Iterator](zip2sequence/iterator.md)

## See Also

- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [actor MainActor](mainactor.md)
  A singleton actor whose executor is equivalent to the main dispatch queue.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [protocol SendableMetatype](sendablemetatype.md)
  A type whose metatype can be shared across arbitrary concurrent contexts without introducing a risk of data races. When a generic type `T` conforms to `SendableMetatype`, its metatype `T.Type` conforms to `Sendable`.  All concrete types implicitly conform to the `SendableMetatype` protocol, so its primary purpose is in generic code to prohibit the use of isolated conformances along with the generic type.
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sendable)*