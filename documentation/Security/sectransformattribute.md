# SecTransformAttribute

**Framework**: Security  
**Kind**: typealias

A direct reference to a security transform attribute.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typealias SecTransformAttribute = CFTypeRef
```

#### Discussion

Using an attribute reference rather than referring to it by name, such as in calls to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](sectransformcustomsetattribute(_:_:_:_:).md) function, speeds up the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformattribute)*