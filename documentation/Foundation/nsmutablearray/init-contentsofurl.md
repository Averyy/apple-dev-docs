# init(contentsOfURL:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a mutable array containing the contents specified by a given URL.

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
init?(contentsOfURL url: URL)
```

#### Return Value

A mutable array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array.

#### Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable even if the array is mutable.

## Parameters

- `url`: The location of the file containing a string representation of a mutable array produced by the   method.

## See Also

- [func write(to: URL, atomically: Bool) -> Bool](nsarray/write(to:atomically:).md)
  Writes the contents of the array to the location specified by a given URL.
- [init()](nsmutablearray/init.md)
  Initializes a newly allocated array.
- [init(capacity: Int)](nsmutablearray/init(capacity:).md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/init(contentsofurl:))*