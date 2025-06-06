# init(coder:)

**Framework**: Foundation  
**Kind**: init

Creates a predicate by decoding from the coder you specify.

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
init?(coder: NSCoder)
```

## Parameters

- `coder`: The coder to read data from.

## See Also

- [init(andPredicateWithSubpredicates: [NSPredicate])](nscompoundpredicate/init(andpredicatewithsubpredicates:).md)
  Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [init(notPredicateWithSubpredicate: NSPredicate)](nscompoundpredicate/init(notpredicatewithsubpredicate:).md)
  Returns a new predicate that you form using a NOT operation on a specified predicate.
- [init(orPredicateWithSubpredicates: [NSPredicate])](nscompoundpredicate/init(orpredicatewithsubpredicates:).md)
  Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [init(type: NSCompoundPredicate.LogicalType, subpredicates: [NSPredicate])](nscompoundpredicate/init(type:subpredicates:).md)
  Returns the receiver that a specified type initializes using predicates from a specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(coder:))*