# entersReaderIfAvailable

**Framework**: Safari Services  
**Kind**: property

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

#### Discussion

Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) if Reader mode should be entered automatically when it is available for the webpage; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Set this configuration property instead of initializing a view controller with [`init(url:entersReaderIfAvailable:)`](sfsafariviewcontroller/init(url:entersreaderifavailable:).md).

## See Also

- [var barCollapsingEnabled: Bool](sfsafariviewcontroller/configuration-swift.class/barcollapsingenabled.md)
- [var eventAttribution: UIEventAttribution?](sfsafariviewcontroller/configuration-swift.class/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class/entersreaderifavailable)*