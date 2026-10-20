# init(captions:timeRange:conversionSettings:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that validates captions for a conversion operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(captions: [AVCaption], timeRange: CMTimeRange, conversionSettings: [AVCaptionSettingsKey : Any])
```

```objc
- (instancetype) initWithCaptions:(NSArray<AVCaption *> *) captions timeRange:(CMTimeRange) timeRange conversionSettings:(NSDictionary<NSString *,id> *) conversionSettings;
```

## Parameters

- `captions`: The array of captions that the system validates.
- `timeRange`: The time range of the media timeline where the captions exist.
- `conversionSettings`: A dictionary that describes the conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/init(captions:timerange:conversionsettings:))*