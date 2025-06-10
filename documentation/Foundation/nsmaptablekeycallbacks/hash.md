# hash

**Framework**: Foundation  
**Kind**: property

Points to the function which must produce hash code for key elements of the map table. If `NULL`, the pointer value is used as the hash code. Second parameter is the element for which hash code should be produced.

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
var hash: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Int)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/hash)*