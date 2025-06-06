# init(value:minimum:maximum:identifier:)

**Framework**: PHASE  
**Kind**: init

Creates a specification for a named metaparameter with the given numeric value and range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(value: Double, minimum: Double, maximum: Double, identifier: String)
```

## Parameters

- `value`: A default value for the metaparameter specification.
- `minimum`: The lowest possible number for the value.
- `maximum`: The highest possible number for the value.
- `identifier`: A unique name for the metaparameter specification.

## See Also

- [convenience init(value: Double)](phasenumbermetaparameterdefinition/init(value:).md)
  Creates a specification for a metaparameter with the given numeric value.
- [convenience init(value: Double, identifier: String)](phasenumbermetaparameterdefinition/init(value:identifier:).md)
  Creates a specification for a named metaparameter with the given numeric value.
- [init(value: Double, minimum: Double, maximum: Double)](phasenumbermetaparameterdefinition/init(value:minimum:maximum:).md)
  Creates a specification for a metaparameter with the given numeric value and range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameterdefinition/init(value:minimum:maximum:identifier:))*