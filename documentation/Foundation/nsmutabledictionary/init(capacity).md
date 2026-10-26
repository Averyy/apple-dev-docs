# init(capacity:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.

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
init(capacity numItems: Int)
```

```objc
- (instancetype) initWithCapacity:(NSUInteger) numItems;
```

#### Return Value

An initialized mutable dictionary, which might be different than the original receiver.

#### Discussion

Mutable dictionaries allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer of `NSMutableDictionary`.

## Parameters

- `numItems`: The initial capacity of the initialized dictionary.

## See Also

### Creating and Initializing a Mutable Dictionary
- [init()](./init%28%29.md)
  Initializes a newly allocated mutable dictionary.
- [init(sharedKeySet: Any)](./init%28sharedkeyset%29.md)
  Creates a mutable dictionary which is optimized for dealing with a known set of keys.
### Related Documentation
- [+ dictionaryWithCapacity:](./dictionarywithcapacity_.md)
  Creates and returns a mutable dictionary, initially giving it enough allocated memory to hold a given number of entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/init(capacity:))*