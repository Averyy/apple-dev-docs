# entersReaderIfAvailable

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

A value that specifies whether Safari should enter Reader mode, if it is available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var entersReaderIfAvailable: Bool { get set }
```

```objc
@property (nonatomic) BOOL entersReaderIfAvailable;
```

#### Discussion

Set the value to [`true`](../../../Swift/true.md) if Reader mode should be entered automatically when it is available for the webpage; otherwise, [`false`](../../../Swift/false.md). The default value is [`false`](../../../Swift/false.md). Set this configuration property instead of initializing a view controller with [`init(url:entersReaderIfAvailable:)`](../init%28url,entersreaderifavailable%29-3aatz.md).

## See Also

### Configuring a Safari View Controller
- [var barCollapsingEnabled: Bool](./barcollapsingenabled.md)
- [var eventAttribution: UIEventAttribution?](./eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class/entersreaderifavailable)*