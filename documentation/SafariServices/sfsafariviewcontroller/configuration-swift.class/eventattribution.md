# eventAttribution

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

An object you use to send tap event attribution data to the browser for Private Click Measurement.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var eventAttribution: UIEventAttribution? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIEventAttribution * eventAttribution;
```

## Discussion

For more information about preparing event attribution data, see [`UIEventAttribution`](../../../UIKit/uieventattribution.md).

## See Also

### Configuring a Safari View Controller
- [var entersReaderIfAvailable: Bool](./entersreaderifavailable.md)
  A value that specifies whether Safari should enter Reader mode, if it is available.
- [var barCollapsingEnabled: Bool](./barcollapsingenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class/eventattribution)*