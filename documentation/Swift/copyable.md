# Copyable

**Framework**: Swift  
**Kind**: protocol

A type whose values can be implicitly or explicitly copied.

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
protocol Copyable
```

#### Overview

Conforming to this protocol indicates that a type’s value can be copied; this protocol doesn’t have any required methods or properties. You don’t generally need to write an explicit conformance to `Copyable`. The following places implicitly include `Copyable` conformance:

- Structure declarations, unless it has a noncopyable stored property
- Enumeration declarations, unless it has a case whose associated value isn’t copyable
- Class declarations
- Actor declarations
- Protocol declarations
- Associated type declarations
- The `Self` type in a protocol extension
- In an extension, the generic parameters of the type being extended

A class or actor can contain noncopyable stored properties, while still being copyable itself — classes and actors are copied by retaining and releasing references.

In a declaration that includes generic type parameters, each generic type parameter implicitly includes `Copyable` in its list of requirements. Metatypes and tuples of copyable types are also implicitly copyable, as are boxed protocol types. For example, all of the following pairs of declarations are equivalent:

```swift
struct MyStructure { }
struct MyStructere: Copyable { }

protocol MyProtocol { }
protocol MyProtocol: Copyable { }

protocol AnotherProtocol {
    associatedtype MyType
    associatedtype MyType: Copyable
}

func genericFunction<T>(t: T) { }
func genericFunction<T>(t: T) where T: Copyable { }

let x: any MyProtocol
let x: any MyProtocol & Copyable
```

To suppress an implicit conformance to `Copyable` you write `~Copyable`. For example, only copyable types can conform to `MyProtocol` in the example above, but both copyable and noncopyable types can conform `NoRequirements` in the example below:

```swift
protocol NoRequirements: ~Copyable { }
```

Extensions to the `Copyable` protocol are not allowed.

## Relationships

### Conforming Types
- [Anchor](../regexbuilder/anchor.md)
- [AnyBidirectionalCollection](anybidirectionalcollection.md)
- [AnyCollection](anycollection.md)
- [AnyHashable](anyhashable.md)
- [AnyIndex](anyindex.md)
- [AnyIterator](anyiterator.md)
- [AnyKeyPath](anykeypath.md)
- [AnyRandomAccessCollection](anyrandomaccesscollection.md)
- [AnyRegexOutput](anyregexoutput.md)
- [AnySequence](anysequence.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [AsyncCompactMapSequence](asynccompactmapsequence.md)
- [AsyncDropFirstSequence](asyncdropfirstsequence.md)
- [AsyncDropWhileSequence](asyncdropwhilesequence.md)
- [AsyncFilterSequence](asyncfiltersequence.md)
- [AsyncFlatMapSequence](asyncflatmapsequence.md)
- [AsyncMapSequence](asyncmapsequence.md)
- [AsyncPrefixSequence](asyncprefixsequence.md)
- [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
- [AsyncStream](asyncstream.md)
- [AsyncStream.Continuation.Termination](asyncstream/continuation/termination.md)
- [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
- [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
- [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
- [AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
- [AsyncThrowingStream](asyncthrowingstream.md)
- [AtomicLoadOrdering](../synchronization/atomicloadordering.md)
- [AtomicStoreOrdering](../synchronization/atomicstoreordering.md)
- [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md)
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)
- [Bool](bool.md)
- [CVaListPointer](cvalistpointer.md)
- [Capture](../regexbuilder/capture.md)
- [Character](character.md)
- [CharacterClass](../regexbuilder/characterclass.md)
- [ChoiceOf](../regexbuilder/choiceof.md)
- [ClosedRange](closedrange.md)
- [ClosedRange.Index](closedrange/index.md)
- [CollectionDifference](collectiondifference.md)
- [CollectionDifference.Change](collectiondifference/change.md)
- [CollectionDifference.Index](collectiondifference/index.md)
- [CollectionOfOne](collectionofone.md)
- [CollectionOfOne.Iterator](collectionofone/iterator.md)
- [ContiguousArray](contiguousarray.md)
- [ContinuousClock](continuousclock.md)
- [ContinuousClock.Instant](continuousclock/instant.md)
- [DecodingError](decodingerror.md)
- [DefaultIndices](defaultindices.md)
- [DefaultStringInterpolation](defaultstringinterpolation.md)
- [Dictionary](dictionary.md)
- [Dictionary.Index](dictionary/index.md)
- [Dictionary.Iterator](dictionary/iterator.md)
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
- [Dictionary.Values](dictionary/values-swift.struct.md)
- [DiscardingTaskGroup](discardingtaskgroup.md)
- [DiscontiguousSlice](discontiguousslice.md)
- [DiscontiguousSlice.Index](discontiguousslice/index.md)
- [Double](double.md)
- [DropFirstSequence](dropfirstsequence.md)
- [DropWhileSequence](dropwhilesequence.md)
- [DropWhileSequence.Iterator](dropwhilesequence/iterator.md)
- [Duration](duration.md)
- [Duration.TimeFormatStyle](duration/timeformatstyle.md)
- [Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct.md)
- [Duration.UnitsFormatStyle](duration/unitsformatstyle.md)
- [Duration.UnitsFormatStyle.Attributed](duration/unitsformatstyle/attributed-swift.struct.md)
- [EmptyCollection](emptycollection.md)
- [EmptyCollection.Iterator](emptycollection/iterator.md)
- [EncodingError](encodingerror.md)
- [EnumeratedSequence](enumeratedsequence.md)
- [EnumeratedSequence.Iterator](enumeratedsequence/iterator.md)
- [ExecuteDistributedTargetError.ErrorCode](../distributed/executedistributedtargeterror/errorcode-swift.enum.md)
- [FlattenSequence](flattensequence.md)
- [FlattenSequence.Index](flattensequence/index.md)
- [FlattenSequence.Iterator](flattensequence/iterator.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [FloatingPointClassification](floatingpointclassification.md)
- [FloatingPointRoundingRule](floatingpointroundingrule.md)
- [FloatingPointSign](floatingpointsign.md)
- [Hasher](hasher.md)
- [IndexingIterator](indexingiterator.md)
- [Int](int.md)
- [Int.Words](int/words-swift.struct.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int16.Words](int16/words-swift.struct.md)
- [Int32](int32.md)
- [Int32.Words](int32/words-swift.struct.md)
- [Int64](int64.md)
- [Int64.Words](int64/words-swift.struct.md)
- [Int8](int8.md)
- [Int8.Words](int8/words-swift.struct.md)
- [IteratorSequence](iteratorsequence.md)
- [JobPriority](jobpriority.md)
- [JoinedSequence](joinedsequence.md)
- [JoinedSequence.Iterator](joinedsequence/iterator.md)
- [KeyValuePairs](keyvaluepairs.md)
- [LazyDropWhileSequence](lazydropwhilesequence.md)
- [LazyDropWhileSequence.Iterator](lazydropwhilesequence/iterator.md)
- [LazyFilterSequence](lazyfiltersequence.md)
- [LazyFilterSequence.Iterator](lazyfiltersequence/iterator.md)
- [LazyMapSequence](lazymapsequence.md)
- [LazyMapSequence.Iterator](lazymapsequence/iterator.md)
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
- [LazyPrefixWhileSequence.Index](lazyprefixwhilesequence/index.md)
- [LazyPrefixWhileSequence.Iterator](lazyprefixwhilesequence/iterator.md)
- [LazySequence](lazysequence.md)
- [Local](../regexbuilder/local.md)
- [Lookahead](../regexbuilder/lookahead.md)
- [ManagedBufferPointer](managedbufferpointer.md)
- [Mirror](mirror.md)
- [Mirror.DisplayStyle](mirror/displaystyle-swift.enum.md)
- [NegativeLookahead](../regexbuilder/negativelookahead.md)
- [Never](never.md)
- [ObjectIdentifier](objectidentifier.md)
- [ObservationRegistrar](../observation/observationregistrar.md)
- [OneOrMore](../regexbuilder/oneormore.md)
- [OpaquePointer](opaquepointer.md)
- [Optional](optional.md)
- [Optional.Publisher](optional/publisher-swift.struct.md)
- [Optionally](../regexbuilder/optionally.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [PrefixSequence](prefixsequence.md)
- [PrefixSequence.Iterator](prefixsequence/iterator.md)
- [Range](range.md)
- [RangeSet](rangeset.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [Repeat](../regexbuilder/repeat.md)
- [Repeated](repeated.md)
- [Result](result.md)
- [Result.Publisher](result/publisher-swift.struct.md)
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
- [Set](set.md)
- [Set.Index](set/index.md)
- [Set.Iterator](set/iterator.md)
- [Slice](slice.md)
- [StaticBigInt](staticbigint.md)
- [StaticString](staticstring.md)
- [StrideThrough](stridethrough.md)
- [StrideThroughIterator](stridethroughiterator.md)
- [StrideTo](strideto.md)
- [StrideToIterator](stridetoiterator.md)
- [String](string.md)
- [String.Encoding](string/encoding.md)
- [String.Index](string/index.md)
- [String.IntentInputOptions.CapitalizationType](string/intentinputoptions/capitalizationtype-swift.enum.md)
- [String.IntentInputOptions.KeyboardType](string/intentinputoptions/keyboardtype-swift.enum.md)
- [String.LocalizationValue](string/localizationvalue.md)
- [String.UTF16View](string/utf16view.md)
- [String.UTF8View](string/utf8view.md)
- [String.UnicodeScalarView](string/unicodescalarview.md)
- [Substring](substring.md)
- [Substring.UTF16View](substring/utf16view.md)
- [Substring.UTF8View](substring/utf8view.md)
- [Substring.UnicodeScalarView](substring/unicodescalarview.md)
- [SuspendingClock](suspendingclock.md)
- [SuspendingClock.Instant](suspendingclock/instant.md)
- [SystemRandomNumberGenerator](systemrandomnumbergenerator.md)
- [Task](task.md)
- [TaskGroup](taskgroup.md)
- [TaskPriority](taskpriority.md)
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md)
- [ThrowingTaskGroup](throwingtaskgroup.md)
- [TryCapture](../regexbuilder/trycapture.md)
- [UInt](uint.md)
- [UInt.Words](uint/words-swift.struct.md)
- [UInt128](uint128.md)
- [UInt128.Words](uint128/words-swift.struct.md)
- [UInt16](uint16.md)
- [UInt16.Words](uint16/words-swift.struct.md)
- [UInt32](uint32.md)
- [UInt32.Words](uint32/words-swift.struct.md)
- [UInt64](uint64.md)
- [UInt64.Words](uint64/words-swift.struct.md)
- [UInt8](uint8.md)
- [UInt8.Words](uint8/words-swift.struct.md)
- [UnboundedRange_](unboundedrange_.md)
- [Unicode.ASCII](unicode/ascii.md)
- [Unicode.ASCII.Parser](unicode/ascii/parser.md)
- [Unicode.GeneralCategory](unicode/generalcategory.md)
- [Unicode.NumericType](unicode/numerictype.md)
- [Unicode.Scalar](unicode/scalar.md)
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
- [UnicodeDecodingResult](unicodedecodingresult.md)
- [Unmanaged](unmanaged.md)
- [UnownedJob](unownedjob.md)
- [UnownedSerialExecutor](unownedserialexecutor.md)
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [UnsafeBufferPointer](unsafebufferpointer.md)
- [UnsafeBufferPointer.Iterator](unsafebufferpointer/iterator.md)
- [UnsafeContinuation](unsafecontinuation.md)
- [UnsafeCurrentTask](unsafecurrenttask.md)
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md)
- [UnsafeRawBufferPointer.Iterator](unsaferawbufferpointer/iterator.md)
- [UnsafeRawPointer](unsaferawpointer.md)
- [WordPair](../synchronization/wordpair.md)
- [ZeroOrMore](../regexbuilder/zeroormore.md)
- [Zip2Sequence](zip2sequence.md)
- [Zip2Sequence.Iterator](zip2sequence/iterator.md)

## See Also

- [protocol BitwiseCopyable](bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/copyable)*