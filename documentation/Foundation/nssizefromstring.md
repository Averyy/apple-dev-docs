# NSSizeFromString(_:)

**Framework**: Foundation  
**Kind**: func

Returns an `NSSize` from a text-based representation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSSizeFromString(_ aString: String) -> NSSize
```

#### Discussion

Scans `aString` for two numbers which are used as the width and height, in that order, to create an `NSSize` struct. If `aString` only contains a single number, it is used as the width. The `aString` argument should be formatted like the output of [`NSStringFromSize(_:)`](nsstringfromsize(_:).md), for example, `@"{10,20}"`. If `aString` does not contain any numbers, this function returns an `NSSize` struct whose width and height are both `0`.

## See Also

- [func NSEqualSizes(NSSize, NSSize) -> Bool](nsequalsizes(_:_:).md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](nsmakesize(_:_:).md)
  Returns a new `NSSize` from the specified values.
- [func NSStringFromSize(NSSize) -> String](nsstringfromsize(_:).md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](nssizefromcgsize(_:).md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](nssizetocgsize(_:).md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssizefromstring(_:))*