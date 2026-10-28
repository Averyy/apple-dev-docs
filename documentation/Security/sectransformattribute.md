# SecTransformAttribute

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A direct reference to a security transform attribute.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
typealias SecTransformAttribute = CFTypeRef
```

```c
typedef CFTypeRef SecTransformAttributeRef;
```

## Discussion

Using an attribute reference rather than referring to it by name, such as in calls to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](./sectransformcustomsetattribute%28_,_,_,_%29.md) function, speeds up the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformattribute)*