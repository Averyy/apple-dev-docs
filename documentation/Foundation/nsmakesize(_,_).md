# NSMakeSize(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a new `NSSize` from the specified values.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSMakeSize(_ w: Double, _ h: Double) -> NSSize
```

```c
static NSSize NSMakeSize(CGFloat w, CGFloat h);
```

#### Return Value

An `NSSize` having the specified `width` and `height`.

## See Also

### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](./nsequalsizes%28_,_%29.md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSSizeFromString(String) -> NSSize](./nssizefromstring%28_%29.md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](./nsstringfromsize%28_%29.md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmakesize(_:_:))*