# init(bytesNoCopy:length:encoding:deallocator:)

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
convenience init?(bytesNoCopy bytes: UnsafeMutableRawPointer, length len: Int, encoding: UInt, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(bytesnocopy:length:encoding:deallocator:))*