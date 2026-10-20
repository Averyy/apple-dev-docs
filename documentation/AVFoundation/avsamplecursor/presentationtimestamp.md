# presentationTimeStamp

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The presentation timestamp of the sample at the current position of the cursor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var presentationTimeStamp: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime presentationTimeStamp;
```

## See Also

### Getting timestamps
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The decode timestamp of the sample at the current position of the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/presentationtimestamp)*