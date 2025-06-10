# describe

**Framework**: Foundation  
**Kind**: property

Points to the function which produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.

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
var describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/describe)*