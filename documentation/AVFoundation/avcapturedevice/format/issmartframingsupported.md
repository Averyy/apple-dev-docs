# isSmartFramingSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Returns `true` if smart framing is supported by the current format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isSmartFramingSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSmartFramingSupported) BOOL smartFramingSupported;
```

#### Discussion

An ultra wide camera device that supports dynamic aspect ratio configuration may also support “smart framing monitoring” on particular formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/issmartframingsupported)*