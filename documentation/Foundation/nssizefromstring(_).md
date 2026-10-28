# NSSizeFromString(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns an `NSSize` from a text-based representation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSSizeFromString(_ aString: String) -> NSSize
```

```c
extern NSSize NSSizeFromString(NSString *aString);
```

## Discussion

Scans `aString` for two numbers which are used as the width and height, in that order, to create an `NSSize` struct. If `aString` only contains a single number, it is used as the width. The `aString` argument should be formatted like the output of [`NSStringFromSize(_:)`](./nsstringfromsize%28_%29.md), for example, `@"{10,20}"`. If `aString` does not contain any numbers, this function returns an `NSSize` struct whose width and height are both `0`.

## See Also

### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](./nsequalsizes%28_,_%29.md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](./nsmakesize%28_,_%29.md)
  Returns a new `NSSize` from the specified values.
- [func NSStringFromSize(NSSize) -> String](./nsstringfromsize%28_%29.md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssizefromstring(_:))*