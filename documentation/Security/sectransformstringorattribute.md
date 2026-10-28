# SecTransformStringOrAttribute

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A type that may be either a string or an attribute reference.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
typealias SecTransformStringOrAttribute = CFTypeRef
```

```c
typedef CFTypeRef SecTransformStringOrAttributeRef;
```

## Discussion

Use a value of this type in place of either a [`CFString`](../CoreFoundation/cfstring.md) or a [`SecTransformAttribute`](./sectransformattribute.md) when referring to transform attributes, such as with the `attribute` parameter in calls to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](./sectransformcustomsetattribute%28_,_,_,_%29.md)  and [`SecTransformCustomGetAttribute(_:_:_:)`](./sectransformcustomgetattribute%28_,_,_%29.md) functions. When using a name, see [Transform Attributes](./transform-attributes.md) for a list of valid key names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformstringorattribute)*