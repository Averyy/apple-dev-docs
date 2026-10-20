# init(notPredicateWithSubpredicate:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a new predicate that you form using a NOT operation on a specified predicate.

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
init(notPredicateWithSubpredicate predicate: NSPredicate)
```

```objc
+ (NSCompoundPredicate *) notPredicateWithSubpredicate:(NSPredicate *) predicate;
```

#### Return Value

A new predicate formed by NOT-ing the predicate specified by `predicate`.

#### Discussion

For applications linked on macOS 10.5 or later, the `subpredicates` array is copied. For applications linked on OS X v10.4, the `subpredicates` array is retained (for binary compatibility).

## Parameters

- `predicate`: A predicate.

## See Also

### Creating Compound Predicates
- [init(andPredicateWithSubpredicates: [NSPredicate])](./init%28andpredicatewithsubpredicates%29.md)
  Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [init(orPredicateWithSubpredicates: [NSPredicate])](./init%28orpredicatewithsubpredicates%29.md)
  Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [init(type: NSCompoundPredicate.LogicalType, subpredicates: [NSPredicate])](./init%28type,subpredicates%29.md)
  Returns the receiver that a specified type initializes using predicates from a specified array.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a predicate by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(notpredicatewithsubpredicate:))*