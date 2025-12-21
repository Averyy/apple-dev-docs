# NSEqualSizes(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean that indicates whether two size values are equal.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSEqualSizes(_ aSize: NSSize, _ bSize: NSSize) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `aSize` and `bSize` are identical, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func NSMakeSize(Double, Double) -> NSSize](nsmakesize(_:_:).md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](nssizefromstring(_:).md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](nsstringfromsize(_:).md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](nssizefromcgsize(_:).md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](nssizetocgsize(_:).md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalsizes(_:_:))*