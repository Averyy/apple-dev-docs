# init(mediaItems:mediaSearch:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent that describes the media items for which to search and where to search for them.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mediaItems: [INMediaItem]?, mediaSearch: INMediaSearch?)
```

```objc
- (instancetype) initWithMediaItems:(NSArray<INMediaItem *> *) mediaItems mediaSearch:(INMediaSearch *) mediaSearch;
```

## Return Value

An initialized intent object or nil if the object could not be created.

## Discussion

The [`INSearchForMediaIntent`](../insearchformediaintent.md) object should include information about the media that accurately represents the content and where to find it.

## Parameters

- `mediaItems`: The media content, such as a song or TV show, that the user is playing. When donating the intent, the system uses only the first item in the array, ignoring the other media items in the array.
- `mediaSearch`: The location in which to search when looking for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintent/init(mediaitems:mediasearch:))*