# orderedSetWithCapacity:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an mutable ordered set with a given initial capacity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) orderedSetWithCapacity:(NSUInteger) numItems;
```

## Return Value

A mutable ordered set with initial capacity to hold `numItems` members.

## Discussion

Mutable ordered sets allocate additional memory as needed, so `numItems` simply establishes the set’s initial capacity.

## Parameters

- `numItems`: The initial capacity of the new ordered set.

## See Also

### Creating a Mutable Ordered Set
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an initialized mutable ordered set with a given initial capacity.
- [init()](./init%28%29.md)
  Initializes a newly allocated mutable ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/orderedsetwithcapacity:)*