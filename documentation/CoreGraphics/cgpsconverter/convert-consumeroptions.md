# convert(_:consumer:options:)

**Framework**: Core Graphics  
**Kind**: method

Uses a PostScript converter to convert PostScript data to PDF data.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func convert(_ provider: CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool
```

#### Return Value

A Boolean value that indicates whether the PostScript conversion completed successfully (`true` if it did).

#### Discussion

The conversion is thread safe, however it is not possible to have more than one conversion job in process within a given address space or process. If a given thread is running a conversion and another thread starts a new conversion, the second conversion will block until the first conversion is complete.

> ❗ **Important**:  Although `CGPSConverterConvert` is thread safe (it uses locks to prevent more than one conversion at a time in the same process), it is not thread safe with respect to the Resource Manager. If your application uses the Resource Manager on a separate thread, you should either use locks to prevent `CGPSConverterConvert` from executing during your usage of the Resource Manager or you should perform your conversions using the Post Script converter in a separate process. In general, you can avoid this issue by using nib files instead of Resource Manager resources.

 Although `CGPSConverterConvert` is thread safe (it uses locks to prevent more than one conversion at a time in the same process), it is not thread safe with respect to the Resource Manager. If your application uses the Resource Manager on a separate thread, you should either use locks to prevent `CGPSConverterConvert` from executing during your usage of the Resource Manager or you should perform your conversions using the Post Script converter in a separate process.

In general, you can avoid this issue by using nib files instead of Resource Manager resources.

## Parameters

- `provider`: A Quartz data provider that supplies PostScript data.
- `consumer`: A Quartz data provider that will receive the resulting PDF data.
- `options`: This parameter should be  ; it is reserved for future expansion of the API.

## See Also

- [func abort() -> Bool](cgpsconverter/abort.md)
  Tells a PostScript converter to abort a conversion at the next available opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter/convert(_:consumer:options:))*