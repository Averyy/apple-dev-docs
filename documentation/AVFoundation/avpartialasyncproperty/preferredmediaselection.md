# preferredMediaSelection

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The default media selections for the media selection groups of an asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection> { get }
```

Available when `Root` inherits `AVAsset`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading media selections
- [static var allMediaSelections: AVAsyncProperty<Root, [AVMediaSelection]>](./allmediaselections.md)
  The available media selections for an asset.
- [static var availableMediaCharacteristicsWithMediaSelectionOptions: AVAsyncProperty<Root, [AVMediaCharacteristic]>](./availablemediacharacteristicswithmediaselectionoptions.md)
  The media characteristics that provide media selection options.
- [func loadMediaSelectionGroup(for: AVMediaCharacteristic, completionHandler: (AVMediaSelectionGroup?, (any Error)?) -> Void)](../avasset/loadmediaselectiongroup%28for,completionhandler%29.md)
  Loads a media selection group that contains one or more options with the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredmediaselection)*