# initWithContentsOfURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initialized a newly allocated mutable array with the contents of the location specified by a given URL.

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
- (NSMutableArray<id> *) initWithContentsOfURL:(NSURL *) url;
```

## Return Value

A mutable array initialized to contain the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array. The returned objects must be different than the original receiver.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`,`NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `url`: The location of a file containing a string representation of a mutable array produced by [`write(to:atomically:)`](../nsarray/write%28to,atomically%29.md) method.

## See Also

### Related Documentation
- [func write(to: URL, atomically: Bool) -> Bool](../nsarray/write%28to,atomically%29.md)
  Writes the contents of the array to the location specified by a given URL.
### Creating and Initializing a Mutable Array
- [+ arrayWithCapacity:](./arraywithcapacity_.md)
  Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.
- [+ arrayWithContentsOfFile:](./arraywithcontentsoffile_.md)
  Creates and returns a mutable array containing the contents of the file specified by the given path.
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
- [- initWithContentsOfFile:](./initwithcontentsoffile_.md)
  Initializes a newly allocated mutable array with the contents of the file specified by a given path


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/initwithcontentsofurl:)*