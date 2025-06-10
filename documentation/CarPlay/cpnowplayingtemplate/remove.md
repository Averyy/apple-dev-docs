# remove(_:)

**Framework**: CarPlay  
**Kind**: method

Removes an observer from receiving Now Playing template events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func remove(_ observer: any CPNowPlayingTemplateObserver)
```

#### Discussion

You must register an observer using the [`add(_:)`](cpnowplayingtemplate/add(_:).md) method before calling this method.

## Parameters

- `observer`: An object that implements the   protocol.

## See Also

- [func add(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/add(_:).md)
  Registers an observer that receives Now Playing template events.
- [protocol CPNowPlayingTemplateObserver](cpnowplayingtemplateobserver.md)
  The methods for responding to the user interacting with the Now Playing template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/remove(_:))*