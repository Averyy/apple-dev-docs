# init(value:minimum:maximum:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithValue:(double) value minimum:(double) minimum maximum:(double) maximum identifier:(NSString *) identifier;
```

## Parameters

- `value`: A default value for the metaparameter specification.
- `minimum`: The lowest possible number for the value.
- `maximum`: The highest possible number for the value.
- `identifier`: A unique name for the metaparameter specification.

## See Also

### Creating a Metaparameter Definition
- [convenience init(value: Double)](./init%28value%29.md)
  Creates a specification for a metaparameter with the given numeric value.
- [convenience init(value: Double, identifier: String)](./init%28value,identifier%29.md)
  Creates a specification for a named metaparameter with the given numeric value.
- [init(value: Double, minimum: Double, maximum: Double)](./init%28value,minimum,maximum%29.md)
  Creates a specification for a metaparameter with the given numeric value and range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenumbermetaparameterdefinition/init(value:minimum:maximum:identifier:))*