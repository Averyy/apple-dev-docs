# init(cStringNoCopy:length:freeWhenDone:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use -initWithCString:encoding: instead

## Declaration

```swift
convenience init?(cStringNoCopy bytes: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone freeBuffer: Bool)
```

```objc
- (id) initWithCStringNoCopy:(char *) bytes length:(NSUInteger) length freeWhenDone:(BOOL) freeBuffer;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(cstringnocopy:length:freewhendone:)-7ssxw)*