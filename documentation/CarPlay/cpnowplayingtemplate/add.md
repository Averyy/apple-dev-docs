# add(_:)

**Framework**: CarPlay  
**Kind**: method

Registers an observer that receives Now Playing template events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func add(_ observer: any CPNowPlayingTemplateObserver)
```

## Parameters

- `observer`: An object that implements the   protocol.

## See Also

- [func remove(any CPNowPlayingTemplateObserver)](cpnowplayingtemplate/remove(_:).md)
  Removes an observer from receiving Now Playing template events.
- [protocol CPNowPlayingTemplateObserver](cpnowplayingtemplateobserver.md)
  The methods for responding to the user interacting with the Now Playing template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/add(_:))*