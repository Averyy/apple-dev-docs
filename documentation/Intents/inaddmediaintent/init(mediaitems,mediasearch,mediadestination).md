# init(mediaItems:mediaSearch:mediaDestination:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent that describes the media items to add and where to add them.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mediaItems: [INMediaItem]?, mediaSearch: INMediaSearch?, mediaDestination: INMediaDestination?)
```

```objc
- (instancetype) initWithMediaItems:(NSArray<INMediaItem *> *) mediaItems mediaSearch:(INMediaSearch *) mediaSearch mediaDestination:(INMediaDestination *) mediaDestination;
```

#### Return Value

An initialized intent object or nil if the object could not be created.

#### Discussion

The [`INAddMediaIntent`](../inaddmediaintent.md) object should include information about the media that accurately represents the content, where to find it, and where to add it.

## Parameters

- `mediaItems`: The media content, such as a song or TV show, that the user is playing. When donating the intent, the system uses only the first item in the array, ignoring the other media items in the array.
- `mediaSearch`: The location in which to search when looking for a media item.
- `mediaDestination`: The location to add the media items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintent/init(mediaitems:mediasearch:mediadestination:))*