# NSStringFromSize(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string representation of a size.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSStringFromSize(_ aSize: NSSize) -> String
```

#### Return Value

A string of the form “{a, b}”, where a and b are the width and height, respectively, of `aSize`.

## See Also

- [func NSEqualSizes(NSSize, NSSize) -> Bool](nsequalsizes(_:_:).md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](nsmakesize(_:_:).md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](nssizefromstring(_:).md)
  Returns an `NSSize` from a text-based representation.
- [func NSSizeFromCGSize(CGSize) -> NSSize](nssizefromcgsize(_:).md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](nssizetocgsize(_:).md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromsize(_:))*