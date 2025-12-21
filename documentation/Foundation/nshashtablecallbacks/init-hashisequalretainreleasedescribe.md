# init(hash:isEqual:retain:release:describe:)

**Framework**: Foundation  
**Kind**: init

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
init(hash: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Int)?, isEqual: ((NSHashTable<AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?, retain: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Void)?, release: ((NSHashTable<AnyObject>, UnsafeMutableRawPointer) -> Void)?, describe: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> String?)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtablecallbacks/init(hash:isequal:retain:release:describe:))*