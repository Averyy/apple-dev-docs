# AudioFormatGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets information about an audio format property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFormatGetPropertyInfo(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code. Returns `noErr` if successful.

## Parameters

- `inPropertyID`: An   constant.
- `inSpecifierSize`: The size of the specifier data.
- `inSpecifier`: A buffer of data used as an input argument for querying some of the properties.
- `outPropertyDataSize`: The the size in bytes of the current value of the property. To get the property value, you need a buffer of this size.

## See Also

- [func AudioFormatGetProperty(AudioFormatPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?) -> OSStatus](audioformatgetproperty(_:_:_:_:_:).md)
  Gets the value of an audio format property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioformatgetpropertyinfo(_:_:_:_:))*