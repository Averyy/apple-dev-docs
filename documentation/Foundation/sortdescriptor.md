# SortDescriptor

**Framework**: Foundation  
**Kind**: struct

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
- [init?(NSSortDescriptor, comparing: Compared.Type)](sortdescriptor/init(_:comparing:).md)
  Creates a sort descriptor using a sort descriptor and a type that you specify.
### Inspecting Sort Descriptors
- [var order: SortOrder](sortdescriptor/order.md)
  The sort order that the sort descriptor uses to compare.
### Initializers
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator)](sortdescriptor/init(_:comparator:)-16bsg.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator)](sortdescriptor/init(_:comparator:)-1xorc.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator)](sortdescriptor/init(_:comparator:)-7vg3x.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator)](sortdescriptor/init(_:comparator:)-9m8l9.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator, order: SortOrder)](sortdescriptor/init(_:comparator:order:)-2ouai.md)
- [init(any KeyPath<Compared, String> & Sendable, comparator: String.StandardComparator, order: SortOrder)](sortdescriptor/init(_:comparator:order:)-4qaip.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator, order: SortOrder)](sortdescriptor/init(_:comparator:order:)-76h8b.md)
- [init(any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator, order: SortOrder)](sortdescriptor/init(_:comparator:order:)-pz7l.md)
- [init(any KeyPath<Compared, Double> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-1t1a5.md)
- [init(any KeyPath<Compared, UInt?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-29e6k.md)
- [init(any KeyPath<Compared, Float?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-29pto.md)
- [init(any KeyPath<Compared, Int8> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-2u61k.md)
- [init(any KeyPath<Compared, Int32?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-3fgjr.md)
- [init(any KeyPath<Compared, UUID?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-3iwfh.md)
- [init(any KeyPath<Compared, UInt64?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-3wlt2.md)
- [init<Value>(any KeyPath<Compared, Value?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-3wozy.md)
- [init(any KeyPath<Compared, UInt16> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-49ozr.md)
- [init(any KeyPath<Compared, Int16> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-4b7jd.md)
- [init<Value>(any KeyPath<Compared, Value> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-4doe9.md)
- [init(any KeyPath<Compared, Double?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-4uo4r.md)
- [init(any KeyPath<Compared, UUID> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-4z0c9.md)
- [init(any KeyPath<Compared, Int32> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-51msp.md)
- [init(any KeyPath<Compared, UInt64> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-52see.md)
- [init(any KeyPath<Compared, UInt32?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-5lbot.md)
- [init(any KeyPath<Compared, Int> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-5myfn.md)
- [init(any KeyPath<Compared, Bool> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-5s8d4.md)
- [init(any KeyPath<Compared, Int64?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-5y1wt.md)
- [init(any KeyPath<Compared, Date?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-7rdjb.md)
- [init(any KeyPath<Compared, Bool?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-86gfd.md)
- [init(any KeyPath<Compared, UInt32> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-8flg7.md)
- [init(any KeyPath<Compared, Float> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-8jc9k.md)
- [init(any KeyPath<Compared, UInt> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-8tm2c.md)
- [init(any KeyPath<Compared, UInt8> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-95o7r.md)
- [init(any KeyPath<Compared, Int16?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-9noh7.md)
- [init(any KeyPath<Compared, Date> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-9xg3w.md)
- [init(any KeyPath<Compared, UInt16?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-ks7r.md)
- [init(any KeyPath<Compared, UInt8?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-kwgp.md)
- [init(any KeyPath<Compared, Int?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-qlnj.md)
- [init(any KeyPath<Compared, Int64> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-rnot.md)
- [init(any KeyPath<Compared, Int8?> & Sendable, order: SortOrder)](sortdescriptor/init(_:order:)-z7th.md)
### Instance Properties
- [var keyPath: PartialKeyPath<Compared>?](sortdescriptor/keypath.md)
- [var stringComparator: String.StandardComparator?](sortdescriptor/stringcomparator.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SortComparator](sortcomparator.md)

## See Also

- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](comparisonresult.md)
  Constants that indicate sort order.
- [protocol SortComparator](sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortdescriptor)*