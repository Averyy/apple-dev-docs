# Subscribers.Demand

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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

- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)

## Topics

### Creating a demand instance
- [static func max(Int) -> Subscribers.Demand](./demand/max%28_%29.md)
  Creates a demand for the given maximum number of elements.
### Using special demands
- [static let unlimited: Subscribers.Demand](./demand/unlimited.md)
  A request for as many values as the publisher can produce.
- [static let none: Subscribers.Demand](./demand/none.md)
  A request for no elements from the publisher.
### Inspecing demand properties
- [var max: Int?](./demand/max.md)
  The number of requested values.
### Encoding and decoding
- [func encode(to: any Encoder) throws](./demand/encode%28to%29.md)
  Encodes the demand to the provide encoder.
- [init(from: any Decoder) throws](./demand/init%28from%29.md)
  Creates a demand instance from a decoder.
### Performing mathematical operations
- [static func * (Subscribers.Demand, Int) -> Subscribers.Demand](./demand/star%28_,_%29.md)
  Returns the result of multiplying a demand by an integer.
- [static func *= (inout Subscribers.Demand, Int)](./demand/stareq%28_,_%29.md)
  Multiplies a demand by an integer, and assigns the result to the demand.
- [static func + (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](./demand/plus%28_,_%29-2hdad.md)
  Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [static func + (Subscribers.Demand, Int) -> Subscribers.Demand](./demand/plus%28_,_%29-902we.md)
  Returns the result of adding an integer to a demand.
- [static func += (inout Subscribers.Demand, Subscribers.Demand)](./demand/pluseq%28_,_%29-20lis.md)
  Adds two demands, and assigns the result to the first demand.
- [static func += (inout Subscribers.Demand, Int)](./demand/pluseq%28_,_%29-3k1hv.md)
  Adds an integer to a demand, and assigns the result to the demand.
- [static func - (Subscribers.Demand, Subscribers.Demand) -> Subscribers.Demand](./demand/minus%28_,_%29-1r0gm.md)
  Returns the result of subtracting one demand from another.
- [static func - (Subscribers.Demand, Int) -> Subscribers.Demand](./demand/minus%28_,_%29-6mw4s.md)
  Returns the result of subtracting an integer from a demand.
- [static func -= (inout Subscribers.Demand, Subscribers.Demand)](./demand/minuseq%28_,_%29-1d0m9.md)
  Subtracts one demand from another, and assigns the result to the first demand.
- [static func -= (inout Subscribers.Demand, Int)](./demand/minuseq%28_,_%29-9pwnc.md)
  Subtracts an integer from a demand, and assigns the result to the demand.
### Comparing demands
- [static func == (Int, Subscribers.Demand) -> Bool](./demand/eqeq%28_,_%29-4oy8i.md)
  Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [static func == (Subscribers.Demand, Int) -> Bool](./demand/eqeq%28_,_%29-7246z.md)
  Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [static func != (Int, Subscribers.Demand) -> Bool](./demand/noteq%28_,_%29-3j2h8.md)
  Returns a Boolean value that indicates whether an integer is unequal to a demand.
- [static func != (Subscribers.Demand, Int) -> Bool](./demand/noteq%28_,_%29-2dj1p.md)
  Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [static func < (Int, Subscribers.Demand) -> Bool](./demand/op%28_,_%29-1wuod.md)
  Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [static func < (Subscribers.Demand, Int) -> Bool](./demand/op%28_,_%29-ciby.md)
  Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [static func < (Subscribers.Demand, Subscribers.Demand) -> Bool](./demand/op%28_,_%29-8nf1g.md)
  Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [static func <= (Int, Subscribers.Demand) -> Bool](./demand/opeq%28_,_%29-5f62z.md)
  Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [static func <= (Subscribers.Demand, Int) -> Bool](./demand/opeq%28_,_%29-2otvi.md)
  Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [static func <= (Subscribers.Demand, Subscribers.Demand) -> Bool](./demand/opeq%28_,_%29-9cywv.md)
  Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
- [static func > (Int, Subscribers.Demand) -> Bool](./demand/op%28_,_%29-35p6f.md)
  Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [static func > (Subscribers.Demand, Int) -> Bool](./demand/op%28_,_%29-4k1xp.md)
  Returns a Boolean that indicates whether the demand requests more than the given number of elements.
- [static func > (Subscribers.Demand, Subscribers.Demand) -> Bool](./demand/op%28_,_%29-74yle.md)
  Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [static func >= (Int, Subscribers.Demand) -> Bool](./demand/opeq%28_,_%29-6lv9s.md)
  Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [static func >= (Subscribers.Demand, Int) -> Bool](./demand/opeq%28_,_%29-28c1e.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [static func >= (Subscribers.Demand, Subscribers.Demand) -> Bool](./demand/opeq%28_,_%29-5xnt.md)
  Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand)*