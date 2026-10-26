# arrayWithCapacity:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.

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
+ (instancetype) arrayWithCapacity:(NSUInteger) numItems;
```

#### Return Value

A new `NSMutableArray` object with enough allocated memory to hold `numItems` objects.

#### Discussion

Mutable arrays expand as needed; `numItems` simply establishes the object’s initial capacity.

## Parameters

- `numItems`: The initial capacity of the new array.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
### Creating and Initializing a Mutable Array
- [+ arrayWithContentsOfFile:](./arraywithcontentsoffile_.md)
  Creates and returns a mutable array containing the contents of the file specified by the given path.
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
- [- initWithContentsOfFile:](./initwithcontentsoffile_.md)
  Initializes a newly allocated mutable array with the contents of the file specified by a given path
- [- initWithContentsOfURL:](./initwithcontentsofurl_.md)
  Initialized a newly allocated mutable array with the contents of the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/arraywithcapacity:)*