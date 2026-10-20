# init(orPredicateWithSubpredicates:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a new predicate that you form using an OR operation on the predicates in a specified array.

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
init(orPredicateWithSubpredicates subpredicates: [NSPredicate])
```

```objc
+ (NSCompoundPredicate *) orPredicateWithSubpredicates:(NSArray<NSPredicate *> *) subpredicates;
```

#### Return Value

A new predicate formed by OR-ing the predicates specified by `subpredicates`.

#### Discussion

An OR predicate with no subpredicates evaluates to FALSE.

##### Special Considerations

For applications linked on macOS 10.5 or later, the `subpredicates` array is copied. For applications linked on OS X v10.4, the `subpredicates` array is retained (for binary compatibility).

## Parameters

- `subpredicates`: An array of `NSPredicate` objects.

## See Also

### Creating Compound Predicates
- [init(andPredicateWithSubpredicates: [NSPredicate])](./init%28andpredicatewithsubpredicates%29.md)
  Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [init(notPredicateWithSubpredicate: NSPredicate)](./init%28notpredicatewithsubpredicate%29.md)
  Returns a new predicate that you form using a NOT operation on a specified predicate.
- [init(type: NSCompoundPredicate.LogicalType, subpredicates: [NSPredicate])](./init%28type,subpredicates%29.md)
  Returns the receiver that a specified type initializes using predicates from a specified array.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a predicate by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(orpredicatewithsubpredicates:))*