# init(charactersNoCopy:length:deallocator:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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
convenience init(charactersNoCopy chars: UnsafeMutablePointer<unichar>, length len: Int, deallocator: ((UnsafeMutablePointer<unichar>, Int) -> Void)? = nil)
```

```objc
- (instancetype) initWithCharactersNoCopy:(unichar *) chars length:(NSUInteger) len deallocator:(void (^)(unichar *, NSUInteger )) deallocator;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(charactersnocopy:length:deallocator:))*