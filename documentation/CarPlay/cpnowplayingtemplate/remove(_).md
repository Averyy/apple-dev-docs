# remove(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Removes an observer from receiving Now Playing template events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func remove(_ observer: any CPNowPlayingTemplateObserver)
```

```objc
- (void) removeObserver:(id<CPNowPlayingTemplateObserver>) observer;
```

#### Discussion

You must register an observer using the [`add(_:)`](./add%28_%29.md) method before calling this method.

## Parameters

- `observer`: An object that implements the [`CPNowPlayingTemplateObserver`](../cpnowplayingtemplateobserver.md) protocol.

## See Also

### Observing Now Playing Events
- [func add(any CPNowPlayingTemplateObserver)](./add%28_%29.md)
  Registers an observer that receives Now Playing template events.
- [protocol CPNowPlayingTemplateObserver](../cpnowplayingtemplateobserver.md)
  The methods for responding to the user interacting with the Now Playing template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/remove(_:))*