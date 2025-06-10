# isEqual

**Framework**: Foundation  
**Kind**: property

Points to the function which compares second and third parameters. If `NULL`, then == is used for comparison.

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
var isEqual: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/isequal)*