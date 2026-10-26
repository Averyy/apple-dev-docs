# captionFormatConformerWithConversionSettings:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

A class method that creates a new object with format conversion settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
+ (instancetype) captionFormatConformerWithConversionSettings:(NSDictionary<NSString *,id> *) conversionSettings;
```

#### Return Value

A new instance of [`AVCaptionFormatConformer`](../avcaptionformatconformer.md).

## Parameters

- `conversionSettings`: A dictionary that specifies the conversion settings that this instance uses.

## See Also

### Creating a format conformer
- [init(conversionSettings: [AVCaptionSettingsKey : Any])](./init%28conversionsettings%29.md)
  Creates a new object with format conversion settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/captionformatconformerwithconversionsettings:)*