# Subscribers.Demand

**Framework**: Combine  
**Kind**: struct

A requested number of items, sent to a publisher from a subscriber through the subscription.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Demand
```

## Mentions

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md)

## Topics

### Creating a Demand
- [static func max(Int) -> Subscribers.Demand](subscribers/demand/max(_:).md)
  Creates a demand for the given maximum number of elements.
### Using Special Demands
- [static let unlimited: Subscribers.Demand](subscribers/demand/unlimited.md)
  A request for as many values as the publisher can produce.
- [static let none: Subscribers.Demand](subscribers/demand/none.md)
  A request for no elements from the publisher.
### Inspecing Demand Properties
- [var max: Int?](subscribers/demand/max.md)
  The number of requested values.
### Encoding and Decoding
- [func encode(to: any Encoder) throws](subscribers/demand/encode(to:).md)
  Encodes the demand to the provide encoder.
- [init(from: any Decoder) throws](subscribers/demand/init(from:).md)
  Creates a demand instance from a decoder.
### Performing Mathematical Operations
- [static func * (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/*(_:_:).md)
  Returns the result of multiplying a demand by an integer.
- [static func *= (inout Subscribers.Demand, Int)](subscribers/demand/*=(_:_:).md)
  Multiplies a demand by an integer, and assigns the result to the demand.
- [static func + (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](subscribers/demand/+(_:_:)-2hdad.md)
  Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [static func + (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/+(_:_:)-902we.md)
  Returns the result of adding an integer to a demand.
- [static func += (inout Subscribers.Demand, Subscribers.Demand)](subscribers/demand/+=(_:_:)-20lis.md)
  Adds two demands, and assigns the result to the first demand.
- [static func += (inout Subscribers.Demand, Int)](subscribers/demand/+=(_:_:)-3k1hv.md)
  Adds an integer to a demand, and assigns the result to the demand.
- [static func - (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](subscribers/demand/-(_:_:)-1r0gm.md)
  Returns the result of subtracting one demand from another.
- [static func - (Subscribers.Demand, Int) -> Subscribers.Demand](subscribers/demand/-(_:_:)-6mw4s.md)
  Returns the result of subtracting an integer from a demand.
- [static func -= (inout Subscribers.Demand, Subscribers.Demand)](subscribers/demand/-=(_:_:)-1d0m9.md)
  Subtracts one demand from another, and assigns the result to the first demand.
- [static func -= (inout Subscribers.Demand, Int)](subscribers/demand/-=(_:_:)-9pwnc.md)
  Subtracts an integer from a demand, and assigns the result to the demand.
- [static func ... (Self) -> PartialRangeFrom<Self>](subscribers/demand/'...(_:)-3qgos.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](subscribers/demand/'...(_:)-kb35.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](subscribers/demand/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
### Comparing Demands
- [static func == (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-28b3l.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == (Subscribers.Demand, Int) -> Bool](subscribers/demand/==(_:_:)-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func == (Int, Subscribers.Demand) -> Bool](subscribers/demand/==(_:_:)-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func != (Self, Self) -> Bool](subscribers/demand/!=(_:_:)-5u2pg.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func != (Subscribers.Demand, Int) -> Bool](subscribers/demand/!=(_:_:)-2dj1p.md)
  Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [static func != (Int, Subscribers.Demand) -> Bool](subscribers/demand/!=(_:_:)-3j2h8.md)
  Returns a Boolean value that indicates whether an integer is unequal to a demand.
### Operators
- [static func < (Int, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-1wuod.md)
  Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [static func > (Int, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-35p6f.md)
  Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [static func > (Subscribers.Demand, Int) -> Bool](subscribers/demand/_(_:_:)-4k1xp.md)
  Returns a Boolean that indicates whether the demand requests more than the given number of elements.
- [static func > (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-74yle.md)
  Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [static func < (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_(_:_:)-8nf1g.md)
  Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [static func < (Subscribers.Demand, Int) -> Bool](subscribers/demand/_(_:_:)-ciby.md)
  Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [static func >= (Subscribers.Demand, Int) -> Bool](subscribers/demand/_=(_:_:)-28c1e.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [static func <= (Subscribers.Demand, Int) -> Bool](subscribers/demand/_=(_:_:)-2otvi.md)
  Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [static func <= (Int, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-5f62z.md)
  Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [static func >= (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-5xnt.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [static func >= (Int, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-6lv9s.md)
  Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [static func <= (Subscribers.Demand, Subscribers.Demand) -> Bool](subscribers/demand/_=(_:_:)-9cywv.md)
  Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
### Instance Properties
- [var description: String](subscribers/demand/description.md)
  A textual representation of this instance.
- [var hashValue: Int](subscribers/demand/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](subscribers/demand/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Comparable Implementations](subscribers/demand/comparable-implementations.md)
- [Equatable Implementations](subscribers/demand/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand)*