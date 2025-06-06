# preferredMediaSelection

**Framework**: AVFoundation  
**Kind**: property

The default media selections for the media selection groups of an asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [static var allMediaSelections: AVAsyncProperty<Root, [AVMediaSelection]>](avpartialasyncproperty/allmediaselections.md)
  The available media selections for an asset.
- [static var availableMediaCharacteristicsWithMediaSelectionOptions: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md)
  The media characteristics that provide media selection options.
- [func loadMediaSelectionGroup(for: AVMediaCharacteristic, completionHandler: (AVMediaSelectionGroup?, (any Error)?) -> Void)](avasset/loadmediaselectiongroup(for:completionhandler:).md)
  Loads a media selection group that contains one or more options with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredmediaselection)*