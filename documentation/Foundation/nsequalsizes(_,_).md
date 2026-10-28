# NSEqualSizes(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean that indicates whether two size values are equal.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSEqualSizes(_ aSize: NSSize, _ bSize: NSSize) -> Bool
```

```c
extern BOOL NSEqualSizes(NSSize aSize, NSSize bSize);
```

## Return Value

[`true`](../Swift/true.md) if `aSize` and `bSize` are identical, otherwise [`false`](../Swift/false.md).

## See Also

### Managing Sizes
- [func NSMakeSize(Double, Double) -> NSSize](./nsmakesize%28_,_%29.md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](./nssizefromstring%28_%29.md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](./nsstringfromsize%28_%29.md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](./nssizefromcgsize%28_%29.md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](./nssizetocgsize%28_%29.md)
  Returns a `CGSize` typecast from an `NSSize`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalsizes(_:_:))*