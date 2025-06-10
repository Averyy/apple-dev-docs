# cStringPersonality

**Framework**: Foundation  
**Kind**: property

Use a string hash and `strcmp`; C-string ‘`%s`’ style description.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var cStringPersonality: NSPointerFunctions.Options { get }
```

## See Also

- [static var integerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var objectPointerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](nspointerfunctions/options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](nspointerfunctions/options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](nspointerfunctions/sizefunction.md)).
- [static var integerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var objectPointerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](nspointerfunctions/options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](nspointerfunctions/options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](nspointerfunctions/sizefunction.md)).
- [let NSMapTableObjectPointerPersonality: NSPointerFunctions.Options](nsmaptableobjectpointerpersonality.md)
  Equivalent to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/cstringpersonality)*