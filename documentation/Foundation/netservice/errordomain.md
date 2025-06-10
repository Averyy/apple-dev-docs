# errorDomain

**Framework**: Foundation  
**Kind**: property

This key identifies the originator of the error, which is either the `NSNetService` object or the mach network layer. For most errors, you should not need the value provided by this key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class let errorDomain: String
```

## See Also

- [class let errorCode: String](netservice/errorcode-swift.type.property.md)
  This key identifies the error that occurred during the most recent operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/errordomain)*