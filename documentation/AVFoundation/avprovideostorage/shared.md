# shared

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Returns the singleton instance for Pro Video Storage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class var shared: AVProVideoStorage? { get }
```

```objc
@property (class, readonly, nullable) AVProVideoStorage * sharedStorage;
```

#### Return Value

An instance of the Pro Video Storage class if supported; otherwise, `nil`.

## See Also

### Getting the shared storage
- [class var isSupported: Bool](./issupported.md)
  Whether Pro Video Storage is supported in its current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/shared)*