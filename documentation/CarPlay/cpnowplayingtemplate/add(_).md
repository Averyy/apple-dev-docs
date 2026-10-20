# add(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Registers an observer that receives Now Playing template events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func add(_ observer: any CPNowPlayingTemplateObserver)
```

```objc
- (void) addObserver:(id<CPNowPlayingTemplateObserver>) observer;
```

## Parameters

- `observer`: An object that implements the [`CPNowPlayingTemplateObserver`](../cpnowplayingtemplateobserver.md) protocol.

## See Also

### Observing Now Playing Events
- [func remove(any CPNowPlayingTemplateObserver)](./remove%28_%29.md)
  Removes an observer from receiving Now Playing template events.
- [protocol CPNowPlayingTemplateObserver](../cpnowplayingtemplateobserver.md)
  The methods for responding to the user interacting with the Now Playing template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/add(_:))*