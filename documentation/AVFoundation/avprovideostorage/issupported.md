# isSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Whether Pro Video Storage is supported in its current configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class var isSupported: Bool { get }
```

```objc
@property (class, readonly, getter=isSupported) BOOL supported;
```

#### Return Value

`YES` if the device and OS support Pro Video Storage functionality; otherwise, `NO`.

## See Also

### Getting the shared storage
- [class var shared: AVProVideoStorage?](./shared.md)
  Returns the singleton instance for Pro Video Storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/issupported)*