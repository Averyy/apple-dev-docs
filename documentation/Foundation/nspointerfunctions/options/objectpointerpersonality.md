# objectPointerPersonality

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.

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
static var objectPointerPersonality: NSPointerFunctions.Options { get }
```

```c
NSPointerFunctionsObjectPointerPersonality
```

#### Discussion

As a special case, if you do not use garbage collection and specify this value in conjunction with [`strongMemory`](./strongmemory.md) then the `NSPointerFunctions` object uses `retain` and `release`.

## See Also

### Personality Options
- [static var cStringPersonality: NSPointerFunctions.Options](./cstringpersonality.md)
  Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [static var integerPersonality: NSPointerFunctions.Options](./integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](./objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](./opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](./structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](../sizefunction.md)).
- [var NSMapTableObjectPointerPersonality: NSPointerFunctions.Options](../../nsmaptableobjectpointerpersonality.md)
  Equivalent to [`objectPointerPersonality`](./objectpointerpersonality.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/objectpointerpersonality)*