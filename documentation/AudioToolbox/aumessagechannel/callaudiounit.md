# callAudioUnit(_:)

**Framework**: Audio Toolbox  
**Kind**: method

Sends an audio unit a custom data message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func callAudioUnit(_ message: [AnyHashable : Any]) -> [AnyHashable : Any]
```

#### Return Value

A dictionary with custom data.

#### Discussion

The valid values for key and value types are `NSArray`, `NSDictionary`, `NSOrderedSet`, `NSSet`, `NSString`, `NSData`, `NSNull`, `NSNumber`, and `NSDate`.

## Parameters

- `message`: The data to send the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumessagechannel/callaudiounit(_:))*