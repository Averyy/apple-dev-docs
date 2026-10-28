# callHostBlock

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

A callback for the audio unit to send a message to the host.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional var callHostBlock: CallHostBlock? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) CallHostBlock callHostBlock;
```

*macOS*

```objc
@property (atomic, copy, nullable) CallHostBlock callHostBlock;
```

## Discussion

The host must set a block on this property to use it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumessagechannel/callhostblock)*