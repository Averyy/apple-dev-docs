# isAppleProRAWSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- tvOS 17.0+

## Declaration

```swift
var isAppleProRAWSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAppleProRAWSupported) BOOL appleProRAWSupported;
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](../capturing-photos-in-raw-and-apple-proraw-formats.md)

## Discussion

This property is key-value observable.

## See Also

### Configuring ProRAW support
- [var isAppleProRAWEnabled: Bool](./isappleprorawenabled.md)
  A Boolean value that indicates whether you’ve configured the photo output to deliver Apple ProRAW formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawsupported)*