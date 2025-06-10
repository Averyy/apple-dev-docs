# weakObjects()

**Framework**: Foundation  
**Kind**: method

Returns a new hash table for storing weak references to its contents.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func weakObjects() -> NSHashTable<ObjectType>
```

#### Return Value

A new hash table that uses the [`weakMemory`](nspointerfunctions/options/weakmemory.md) options and [`objectPersonality`](nspointerfunctions/options/objectpersonality.md) and has an initial capacity of `0`.

## See Also

- [init(options: NSPointerFunctions.Options)](nshashtable/init(options:).md)
  Returns a hash table with given pointer functions options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/weakobjects())*