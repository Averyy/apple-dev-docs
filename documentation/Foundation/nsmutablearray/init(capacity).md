# init(capacity:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an array, initialized with enough memory to initially hold a given number of objects.

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

## Return Value

An array initialized with enough memory to hold `numItems` objects. The returned object might be different than the original receiver.

## Discussion

Mutable arrays expand as needed; `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer.

## Parameters

- `numItems`: The initial capacity of the new array.

## See Also

### Creating and Initializing a Mutable Array
- [init?(contentsOfURL: URL)](./init%28contentsofurl%29.md)
  Creates and returns a mutable array containing the contents specified by a given URL.
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [+ arrayWithContentsOfFile:](./arraywithcontentsoffile_.md)
  Creates and returns a mutable array containing the contents of the file specified by the given path.
- [- initWithContentsOfFile:](./initwithcontentsoffile_.md)
  Initializes a newly allocated mutable array with the contents of the file specified by a given path
- [- initWithContentsOfURL:](./initwithcontentsofurl_.md)
  Initialized a newly allocated mutable array with the contents of the location specified by a given URL.
### Related Documentation
- [+ arrayWithCapacity:](./arraywithcapacity_.md)
  Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/init(capacity:))*