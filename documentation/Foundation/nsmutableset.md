# NSMutableSet

**Framework**: Foundation  
**Kind**: class

A dynamic unordered collection of unique objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMutableSet
```

#### Overview

You can use this type in Swift instead of a [`Set`](https://developer.apple.com/documentation/Swift/Set) in cases that require reference semantics.

The `NSMutableSet` class declares the programmatic interface to a mutable, unordered collection of distinct objects.

The [`NSCountedSet`](nscountedset.md) class, which is a concrete subclass of `NSMutableSet`, supports mutable sets that can contain multiple instances of the same element. The [`NSSet`](nsset.md) class supports creating and managing immutable sets.

NSMutableSet is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableSet`](https://developer.apple.com/documentation/CoreFoundation/CFMutableSet). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it is often better to consider composition instead of subclassing.

###### Methods to Override

In a subclass, you must override both of its primitive methods:

- [`add(_:)`](nsmutableset/add(_:).md)
- [`remove(_:)`](nsmutableset/remove(_:).md)

You must also override the primitive methods of the [`NSSet`](nsset.md) class.

## Topics

### Creating a mutable set
- [init(capacity: Int)](nsmutableset/init(capacity:).md)
  Returns an initialized mutable set with a given initial capacity.
- [init()](nsmutableset/init.md)
  Initializes a newly allocated set.
### Adding and removing entries
- [func add(Any)](nsmutableset/add(_:).md)
  Adds a given object to the set, if it is not already a member.
- [func filter(using: NSPredicate)](nsmutableset/filter(using:).md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func remove(Any)](nsmutableset/remove(_:).md)
  Removes a given object from the set.
- [func removeAllObjects()](nsmutableset/removeallobjects.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](nsmutableset/addobjects(from:).md)
  Adds to the set each object contained in a given array that is not already a member.
### Combining and recombining sets
- [func union(Set<AnyHashable>)](nsmutableset/union(_:).md)
  Adds each object in another given set to the receiving set, if not present.
- [func minus(Set<AnyHashable>)](nsmutableset/minus(_:).md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](nsmutableset/intersect(_:).md)
  Removes from the receiving set each object that isn’t a member of another given set.
- [func setSet(Set<AnyHashable>)](nsmutableset/setset(_:).md)
  Empties the receiving set, then adds each object contained in another given set.
### Initializers
- [init?(coder: NSCoder)](nsmutableset/init(coder:).md)

## Relationships

### Inherits From
- [NSSet](nsset.md)
### Inherited By
- [NSCountedSet](nscountedset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset)*