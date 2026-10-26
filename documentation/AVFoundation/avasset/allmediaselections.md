# allMediaSelections

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The array of available media selections for this asset.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.13+ - Deprecated in 13.0
- tvOS 11.0+ - Deprecated in 16.0
- watchOS 4.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`allMediaSelections`](../avpartialasyncproperty/allmediaselections.md) asynchronously instead.

## Declaration

```swift
var allMediaSelections: [AVMediaSelection] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMediaSelection *> * allMediaSelections;
```

## See Also

### Accessing media selections
- [availableMediaCharacteristicsWithMediaSelectionOptions](./availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.
- [- mediaSelectionGroupForMediaCharacteristic:](./mediaselectiongroup%28formediacharacteristic%29.md)
  Returns a media selection group that contains one or more options with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/allmediaselections)*