# init(capacity:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized mutable ordered set with a given initial capacity.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(capacity numItems: Int)
```

```objc
- (instancetype) initWithCapacity:(NSUInteger) numItems;
```

#### Return Value

An initialized mutable ordered set with initial capacity to hold `numItems` members.

#### Discussion

Mutable ordered sets allocate additional memory as needed, so `numItems` simply establishes the set’s initial capacity.

This method is a designated initializer of `NSMutableOrderedSet`.

## Parameters

- `numItems`: The initial capacity of the new ordered set.

## See Also

### Creating a Mutable Ordered Set
- [init()](./init%28%29.md)
  Initializes a newly allocated mutable ordered set.
### Related Documentation
- [+ orderedSetWithCapacity:](./orderedsetwithcapacity_.md)
  Creates and returns an mutable ordered set with a given initial capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/init(capacity:))*