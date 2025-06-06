# init(dictionary:)

**Framework**: Media Player  
**Kind**: init

Returns a new play parameters object using information from MusicKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init?(dictionary: [String : Any])
```

#### Return Value

A new play parameters object consisting of the information retrieved from MusicKit.

#### Discussion

Create a new `MPMusicPlayerPlayParameters` object using the JSON information returned from a MusicKit query.

## Parameters

- `dictionary`: The JSON information returned from a MusicKit query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparameters/init(dictionary:))*