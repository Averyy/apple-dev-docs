# value

**Framework**: PHASE  
**Kind**: property

A value for the metaparameter.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var value: Any { get set }
```

#### Discussion

The framework sets this property to the subclass’s initializer argument; for example, see [`init(value:)`](phasenumbermetaparameterdefinition/init(value:).md).

An app changes the value at runtime by calling [`fade(value:duration:)`](phasenumbermetaparameter/fade(value:duration:).md) on the subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemetaparameter/value)*