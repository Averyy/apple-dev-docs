# init(contentsOfURL:)

**Framework**: Foundation  
**Kind**: init

Creates and returns an array containing the contents specified by a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(contentsOfURL url: URL)
```

#### Return Value

An array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into an array.

#### Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `url`: The location of a file containing a string representation of an array produced by the   method.

## See Also

- [func write(to: URL, atomically: Bool) -> Bool](nsarray/write(to:atomically:).md)
  Writes the contents of the array to the location specified by a given URL.
- [convenience init(object: Any)](nsarray/init(object:).md)
  Creates and returns an array containing a given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsarray/init(objects:count:)-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(contentsofurl:)-fk8x)*