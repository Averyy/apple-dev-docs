# decomposedStringWithCanonicalMapping

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string made by normalizing the string’s contents using the Unicode Normalization Form D.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var decomposedStringWithCanonicalMapping: String { get }
```

```objc
@property (copy, readonly) NSString * decomposedStringWithCanonicalMapping;
```

## See Also

### Normalizing Strings
- [var decomposedStringWithCompatibilityMapping: String](./decomposedstringwithcompatibilitymapping.md)
  A string made by normalizing the receiver’s contents using the Unicode Normalization Form KD.
- [var precomposedStringWithCanonicalMapping: String](./precomposedstringwithcanonicalmapping.md)
  A string made by normalizing the string’s contents using the Unicode Normalization Form C.
- [var precomposedStringWithCompatibilityMapping: String](./precomposedstringwithcompatibilitymapping.md)
  A string made by normalizing the receiver’s contents using the Unicode Normalization Form KC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/decomposedstringwithcanonicalmapping)*