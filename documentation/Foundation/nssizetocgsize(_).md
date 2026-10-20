# NSSizeToCGSize(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a `CGSize` typecast from an `NSSize`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSSizeToCGSize(_ nssize: NSSize) -> CGSize
```

```c
static CGSize NSSizeToCGSize(NSSize nssize);
```

#### Return Value

A `CGSize` typecast from an `NSSize`.

## See Also

### Related Documentation
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.
- [func NSRectToCGRect(NSRect) -> CGRect](./nsrecttocgrect%28_%29.md)
  Returns a `CGRect` typecast from an `NSRect`.
### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](./nsequalsizes%28_,_%29.md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](./nsmakesize%28_,_%29.md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](./nssizefromstring%28_%29.md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](./nsstringfromsize%28_%29.md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssizetocgsize(_:))*