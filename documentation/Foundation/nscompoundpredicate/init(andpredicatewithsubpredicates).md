# init(andPredicateWithSubpredicates:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a new predicate that you form using an AND operation on the predicates in a specified array.

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
init(andPredicateWithSubpredicates subpredicates: [NSPredicate])
```

```objc
+ (NSCompoundPredicate *) andPredicateWithSubpredicates:(NSArray<NSPredicate *> *) subpredicates;
```

#### Return Value

A new predicate formed by AND-ing the predicates specified by `subpredicates`.

#### Discussion

An AND predicate with no subpredicates evaluates to TRUE.

##### Special Considerations

For applications linked on macOS 10.5 or later, the `subpredicates` array is copied. For applications linked on OS X v10.4, the `subpredicates` array is retained (for binary compatibility).

## Parameters

- `subpredicates`: An array of `NSPredicate` objects.

## See Also

### Related Documentation
- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
### Creating Compound Predicates
- [init(notPredicateWithSubpredicate: NSPredicate)](./init%28notpredicatewithsubpredicate%29.md)
  Returns a new predicate that you form using a NOT operation on a specified predicate.
- [init(orPredicateWithSubpredicates: [NSPredicate])](./init%28orpredicatewithsubpredicates%29.md)
  Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [init(type: NSCompoundPredicate.LogicalType, subpredicates: [NSPredicate])](./init%28type,subpredicates%29.md)
  Returns the receiver that a specified type initializes using predicates from a specified array.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a predicate by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(andpredicatewithsubpredicates:))*