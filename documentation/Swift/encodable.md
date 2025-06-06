# Encodable

**Framework**: Swift  
**Kind**: protocol

A type that can encode itself to an external representation.

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
protocol Encodable
```

## Topics

### Instance Methods
- [func encode(to: any Encoder) throws](encodable/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Inherited By
- [SIMD](simd.md)
### Conforming Types
- [Array](array.md)
- [Bool](bool.md)
- [ClosedRange](closedrange.md)
- [CollectionDifference](collectiondifference.md)
- [CollectionDifference.Change](collectiondifference/change.md)
- [ContiguousArray](contiguousarray.md)
- [ContinuousClock.Instant](continuousclock/instant.md)
- [Dictionary](dictionary.md)
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
- [Float](float.md)
- [Float16](float16.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [LocalTestingActorID](../distributed/localtestingactorid.md)
- [Never](never.md)
- [ObservationRegistrar](../observation/observationregistrar.md)
- [Optional](optional.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [Range](range.md)
- [SIMD16](simd16.md)
- [SIMD2](simd2.md)
- [SIMD3](simd3.md)
- [SIMD32](simd32.md)
- [SIMD4](simd4.md)
- [SIMD64](simd64.md)
- [SIMD8](simd8.md)
- [SIMDMask](simdmask.md)
- [Set](set.md)
- [String](string.md)
- [String.Comparator](string/comparator.md)
- [String.LocalizationValue](string/localizationvalue.md)
- [String.LocalizationValue.Placeholder](string/localizationvalue/placeholder.md)
- [String.StandardComparator](string/standardcomparator.md)
- [SuspendingClock.Instant](suspendingclock/instant.md)
- [TaskPriority](taskpriority.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)

## See Also

- [Encoding and Decoding Custom Types](../Foundation/encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [typealias Codable](codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol Decodable](decodable.md)
  A type that can decode itself from an external representation.
- [protocol CodingKey](codingkey.md)
  A type that can be used as a key for encoding and decoding.
- [protocol CodingKeyRepresentable](codingkeyrepresentable.md)
  A type that can be converted to and from a coding key.
- [struct CodingUserInfoKey](codinguserinfokey.md)
  A user-defined key for providing context during encoding and decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encodable)*