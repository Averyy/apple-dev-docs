# value

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readwrite) id value;
```

## Discussion

The framework sets this property to the subclass’s initializer argument; for example, see [`init(value:)`](../phasenumbermetaparameterdefinition/init%28value%29.md).

An app changes the value at runtime by calling [`fade(value:duration:)`](../phasenumbermetaparameter/fade%28value,duration%29.md) on the subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemetaparameter/value)*