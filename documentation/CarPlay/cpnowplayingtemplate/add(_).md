# add(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Registers an observer to handle events related to the Now Playing interface.

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

## Discussion

Call this method if your app supports the Album Artist or Up Next buttons in the Now Playing interface. The template directs interactions with these buttons to all registered observers.

## Parameters

- `observer`: An object that implements the [`CPNowPlayingTemplateObserver`](../cpnowplayingtemplateobserver.md) protocol.

## See Also

### Adding and removing observers
- [func remove(any CPNowPlayingTemplateObserver)](./remove%28_%29.md)
  Unregisters an observer and stops it from receiving events related to the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/add(_:))*