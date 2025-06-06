# predicateFormat

**Framework**: Foundation  
**Kind**: property

The predicate’s format string.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var predicateFormat: String { get }
```

#### Discussion

The return value of this property is not guaranteed to be the same as the string used to create the predicate using [`predicateWithFormat:`](nspredicate/predicatewithformat:.md) or similar methods.

You cannot use this method to create a persistent representation of a predicate suitable for recreating the original predicate. If you need a persistent representation of a predicate, create an archive instead, as described in [`Object archiving`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1) ([`NSPredicate`](nspredicate.md) adopts the [`NSCoding`](nscoding.md) protocol).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/predicateformat)*