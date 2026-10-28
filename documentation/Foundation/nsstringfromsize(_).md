# NSStringFromSize(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a string representation of a size.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSStringFromSize(_ aSize: NSSize) -> String
```

```c
extern NSString *NSStringFromSize(NSSize aSize);
```

## Return Value

A string of the form “{a, b}”, where a and b are the width and height, respectively, of `aSize`.

## See Also

### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](./nsequalsizes%28_,_%29.md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](./nsmakesize%28_,_%29.md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](./nssizefromstring%28_%29.md)
  Returns an `NSSize` from a text-based representation.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromsize(_:))*