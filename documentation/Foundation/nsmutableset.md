# NSMutableSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMutableSet : NSSet
```

#### Overview

You can use this type in Swift instead of a [`Set`](../Swift/set.md) in cases that require reference semantics.

The `NSMutableSet` class declares the programmatic interface to a mutable, unordered collection of distinct objects.

The [`NSCountedSet`](./nscountedset.md) class, which is a concrete subclass of `NSMutableSet`, supports mutable sets that can contain multiple instances of the same element. The [`NSSet`](./nsset.md) class supports creating and managing immutable sets.

NSMutableSet is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableSet`](../CoreFoundation/cfmutableset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it is often better to consider composition instead of subclassing.

###### Methods to Override

In a subclass, you must override both of its primitive methods:

- [`add(_:)`](./nsmutableset/add%28_%29.md)
- [`remove(_:)`](./nsmutableset/remove%28_%29.md)

You must also override the primitive methods of the [`NSSet`](./nsset.md) class.

## Topics

### Creating a mutable set
- [init(capacity: Int)](./nsmutableset/init%28capacity%29.md)
  Returns an initialized mutable set with a given initial capacity.
- [init()](./nsmutableset/init%28%29.md)
  Initializes a newly allocated set.
### Adding and removing entries
- [func add(Any)](./nsmutableset/add%28_%29.md)
  Adds a given object to the set, if it is not already a member.
- [func filter(using: NSPredicate)](./nsmutableset/filter%28using%29.md)
  Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [func remove(Any)](./nsmutableset/remove%28_%29.md)
  Removes a given object from the set.
- [func removeAllObjects()](./nsmutableset/removeallobjects%28%29.md)
  Empties the set of all of its members.
- [func addObjects(from: [Any])](./nsmutableset/addobjects%28from%29.md)
  Adds to the set each object contained in a given array that is not already a member.
### Combining and recombining sets
- [func union(Set<AnyHashable>)](./nsmutableset/union%28_%29.md)
  Adds each object in another given set to the receiving set, if not present.
- [func minus(Set<AnyHashable>)](./nsmutableset/minus%28_%29.md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](./nsmutableset/intersect%28_%29.md)
  Removes from the receiving set each object that isn’t a member of another given set.
- [func setSet(Set<AnyHashable>)](./nsmutableset/setset%28_%29.md)
  Empties the receiving set, then adds each object contained in another given set.
### Initializers
- [init?(coder: NSCoder)](./nsmutableset/init%28coder%29.md)
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./nsmutableset/init%28objects,count%29.md)

## Relationships

### Inherits From
- [NSSet](./nsset.md)
### Inherited By
- [NSCountedSet](./nscountedset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset)*