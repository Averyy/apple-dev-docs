# loadMediaSelectionGroup(for:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads a media selection group that contains one or more options with the specified media characteristic.

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
func loadMediaSelectionGroup(for mediaCharacteristic: AVMediaCharacteristic) async throws -> AVMediaSelectionGroup?
```

## Parameters

- `mediaCharacteristic`: A media characteristic to load the available media selection options for. The supported characterisics are: - [`audible`](avmediacharacteristic/audible.md) to return the group of available options for audio media in various languages and for various purposes, such as descriptive audio
- [`legible`](avmediacharacteristic/legible.md) to return the group of available options for subtitles in various languages and for various purposes
- [`visual`](avmediacharacteristic/visual.md) to return the group of available options for video media
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **mediaSelectionGroup**: The loaded media selection group, or `nil` if no group is available or if an error occurs.
- **error**: An error object if the request fails; otherwise, `nil`.

## See Also

- [static var allMediaSelections: AVAsyncProperty<Root, [AVMediaSelection]>](avpartialasyncproperty/allmediaselections.md)
  The available media selections for an asset.
- [static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection>](avpartialasyncproperty/preferredmediaselection.md)
  The default media selections for the media selection groups of an asset.
- [static var availableMediaCharacteristicsWithMediaSelectionOptions: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md)
  The media characteristics that provide media selection options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/loadmediaselectiongroup(for:completionhandler:))*