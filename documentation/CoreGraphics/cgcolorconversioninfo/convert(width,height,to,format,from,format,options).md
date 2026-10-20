# convert(width:height:to:format:from:format:options:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func convert(width: Int, height: Int, to dst_data: UnsafeMutableRawPointer, format dst_format: CGColorBufferFormat, from src_data: UnsafeRawPointer, format src_format: CGColorBufferFormat, options: CFDictionary?) -> Bool
```

```c
extern bool CGColorConversionInfoConvertData(CGColorConversionInfoRef info, size_t width, size_t height, void *dst_data, CGColorBufferFormat dst_format, const void *src_data, CGColorBufferFormat src_format, CFDictionaryRef options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/convert(width:height:to:format:from:format:options:))*