# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated mutable dictionary.

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
init()
```

```objc
- (instancetype) init;
```

#### Return Value

A mutable dictionary.

#### Discussion

This method is a designated initializer of `NSMutableDictionary`.

## See Also

### Creating and Initializing a Mutable Dictionary
- [init(capacity: Int)](./init%28capacity%29.md)
  Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [init(sharedKeySet: Any)](./init%28sharedkeyset%29.md)
  Creates a mutable dictionary which is optimized for dealing with a known set of keys.
- [+ dictionaryWithCapacity:](./dictionarywithcapacity_.md)
  Creates and returns a mutable dictionary, initially giving it enough allocated memory to hold a given number of entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/init())*