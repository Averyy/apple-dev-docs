# objectPersonality

**Framework**: Foundation  
**Kind**: property

Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.

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
static var objectPersonality: NSPointerFunctions.Options { get }
```

#### Discussion

This is the default personality value.

As a special case, if you do not use garbage collection and specify this value in conjunction with [`strongMemory`](nspointerfunctions/options/strongmemory.md) then the `NSPointerFunctions` object uses `retain` and `release`.

## See Also

- [static var cStringPersonality: NSPointerFunctions.Options](nspointerfunctions/options/cstringpersonality.md)
  Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [static var integerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPointerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](nspointerfunctions/options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](nspointerfunctions/options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](nspointerfunctions/sizefunction.md)).
- [let NSMapTableObjectPointerPersonality: NSPointerFunctions.Options](nsmaptableobjectpointerpersonality.md)
  Equivalent to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/objectpersonality)*