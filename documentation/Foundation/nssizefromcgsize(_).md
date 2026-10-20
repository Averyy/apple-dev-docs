# NSSizeFromCGSize(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns an `NSSize` typecast from a `CGSize`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSSizeFromCGSize(_ cgsize: CGSize) -> NSSize
```

```c
static NSSize NSSizeFromCGSize(CGSize cgsize);
```

#### Return Value

An `NSSize` typecast from a `CGSize`.

## See Also

### Related Documentation
- [func NSRectFromCGRect(CGRect) -> NSRect](./nsrectfromcgrect%28_%29.md)
  Returns an `NSRect` typecast from a `CGRect`.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.
### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](./nsequalsizes%28_,_%29.md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](./nsmakesize%28_,_%29.md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](./nssizefromstring%28_%29.md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](./nsstringfromsize%28_%29.md)
  Returns a string representation of a size.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssizefromcgsize(_:))*