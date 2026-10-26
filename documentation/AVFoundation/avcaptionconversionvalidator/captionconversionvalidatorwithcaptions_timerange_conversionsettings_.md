# captionConversionValidatorWithCaptions:timeRange:conversionSettings:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

A convenience initializer to create an object that validates captions for a conversion operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
+ (instancetype) captionConversionValidatorWithCaptions:(NSArray<AVCaption *> *) captions timeRange:(CMTimeRange) timeRange conversionSettings:(NSDictionary<NSString *,id> *) conversionSettings;
```

## Parameters

- `captions`: The array of captions that the system validates.
- `timeRange`: The time range of the media timeline where the captions exist.
- `conversionSettings`: A dictionary that describes the conversion operation.

## See Also

### Creating a validator
- [init(captions: [AVCaption], timeRange: CMTimeRange, conversionSettings: [AVCaptionSettingsKey : Any])](./init%28captions,timerange,conversionsettings%29.md)
  Creates an object that validates captions for a conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/captionconversionvalidatorwithcaptions:timerange:conversionsettings:)*