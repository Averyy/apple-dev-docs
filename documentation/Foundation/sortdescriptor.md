# SortDescriptor

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A serializable description of how to sort numerics and strings.

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
struct SortDescriptor<Compared>
```

## Topics

### Creating Sort Descriptors
- [init?(NSSortDescriptor, comparing: Compared.Type)](./sortdescriptor/init%28_,comparing%29.md)
  Creates a sort descriptor using a sort descriptor and a type that you specify.
### Using Sort Descriptors
- [func compare(Compared, Compared) -> ComparisonResult](./sortdescriptor/compare%28_,_%29.md)
  Provides the relative ordering of two elements.
### Inspecting Sort Descriptors
- [var order: SortOrder](./sortdescriptor/order.md)
  The sort order that the sort descriptor uses to compare.
### Initializers
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator)](./sortdescriptor/init%28_,comparator%29-16bsg.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator)](./sortdescriptor/init%28_,comparator%29-1xorc.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator)](./sortdescriptor/init%28_,comparator%29-7vg3x.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator)](./sortdescriptor/init%28_,comparator%29-9m8l9.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator, order: SortOrder)](./sortdescriptor/init%28_,comparator,order%29-2ouai.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator, order: SortOrder)](./sortdescriptor/init%28_,comparator,order%29-4qaip.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator, order: SortOrder)](./sortdescriptor/init%28_,comparator,order%29-76h8b.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator, order: SortOrder)](./sortdescriptor/init%28_,comparator,order%29-pz7l.md)
- [init(any KeyPath<Compared, Double> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-1t1a5.md)
- [init(any KeyPath<Compared, UInt?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-29e6k.md)
- [init(any KeyPath<Compared, Float?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-29pto.md)
- [init(any KeyPath<Compared, Int8> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-2u61k.md)
- [init(any KeyPath<Compared, Int32?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-3fgjr.md)
- [init(any KeyPath<Compared, UUID?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-3iwfh.md)
- [init(any KeyPath<Compared, UInt64?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-3wlt2.md)
- [init<Value>(any KeyPath<Compared, Value?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-3wozy.md)
- [init(any KeyPath<Compared, UInt16> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-49ozr.md)
- [init(any KeyPath<Compared, Int16> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-4b7jd.md)
- [init<Value>(any KeyPath<Compared, Value> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-4doe9.md)
- [init(any KeyPath<Compared, Double?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-4uo4r.md)
- [init(any KeyPath<Compared, UUID> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-4z0c9.md)
- [init(any KeyPath<Compared, Int32> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-51msp.md)
- [init(any KeyPath<Compared, UInt64> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-52see.md)
- [init(any KeyPath<Compared, UInt32?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-5lbot.md)
- [init(any KeyPath<Compared, Int> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-5myfn.md)
- [init(any KeyPath<Compared, Bool> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-5s8d4.md)
- [init(any KeyPath<Compared, Int64?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-5y1wt.md)
- [init(any KeyPath<Compared, Date?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-7rdjb.md)
- [init(any KeyPath<Compared, Bool?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-86gfd.md)
- [init(any KeyPath<Compared, UInt32> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-8flg7.md)
- [init(any KeyPath<Compared, Float> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-8jc9k.md)
- [init(any KeyPath<Compared, UInt> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-8tm2c.md)
- [init(any KeyPath<Compared, UInt8> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-95o7r.md)
- [init(any KeyPath<Compared, Int16?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-9noh7.md)
- [init(any KeyPath<Compared, Date> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-9xg3w.md)
- [init(any KeyPath<Compared, UInt16?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-ks7r.md)
- [init(any KeyPath<Compared, UInt8?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-kwgp.md)
- [init(any KeyPath<Compared, Int?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-qlnj.md)
- [init(any KeyPath<Compared, Int64> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-rnot.md)
- [init(any KeyPath<Compared, Int8?> & Sendable, order: SortOrder)](./sortdescriptor/init%28_,order%29-z7th.md)
### Instance Properties
- [var keyPath: PartialKeyPath<Compared>?](./sortdescriptor/keypath.md)
  The key path to the field for comparison.
- [var stringComparator: String.StandardComparator?](./sortdescriptor/stringcomparator.md)
  A `String.StandardComparator` value.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SortComparator](./sortcomparator.md)

## See Also

### Sorting
- [class NSSortDescriptor](./nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](./comparisonresult.md)
  Constants that indicate sort order.
- [protocol SortComparator](./sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct ComparableComparator](./comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](./keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](./sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortdescriptor)*