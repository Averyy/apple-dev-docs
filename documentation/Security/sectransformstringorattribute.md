# SecTransformStringOrAttribute

**Framework**: Security  
**Kind**: typealias

A type that may be either a string or an attribute reference.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typealias SecTransformStringOrAttribute = CFTypeRef
```

#### Discussion

Use a value of this type in place of either a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) or a [`SecTransformAttribute`](sectransformattribute.md) when referring to transform attributes, such as with the `attribute` parameter in calls to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](sectransformcustomsetattribute(_:_:_:_:).md)  and [`SecTransformCustomGetAttribute(_:_:_:)`](sectransformcustomgetattribute(_:_:_:).md) functions. When using a name, see [`Transform Attributes`](transform-attributes.md) for a list of valid key names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformstringorattribute)*