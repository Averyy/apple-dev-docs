# write(to:atomically:)

**Framework**: Foundation  
**Kind**: method

Writes the contents of the array to the location specified by a given URL.

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
func write(to url: URL, atomically: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the location is written successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the location written by this method can be used to initialize a new array with the class method [`init(contentsOfURL:)`](nsarray/init(contentsofurl:)-fk8x.md) or the instance method [`init(contentsOfURL:)`](nsarray/init(contentsofurl:)-5lo2y.md).

## Parameters

- `url`: The location at which to write the array.
- `atomically`: If  , the array is written to an auxiliary location, and then the auxiliary location is renamed to  . If  , the array is written directly to  . The   option guarantees that  , if it exists at all, won’t be corrupted even if the system should crash during writing.

## See Also

- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](nsarray/write(tofile:atomically:).md)
  Writes the contents of the array to a file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/write(to:atomically:))*