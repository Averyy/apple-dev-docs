# remove(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Unregisters an observer and stops it from receiving events related to the Now Playing interface.

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

## Discussion

Call this method to remove an observer object you previously registered with a call to the [`add(_:)`](./add%28_%29.md) method.

## Parameters

- `observer`: An object you previously registered as an observer.

## See Also

### Adding and removing observers
- [func add(any CPNowPlayingTemplateObserver)](./add%28_%29.md)
  Registers an observer to handle events related to the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/remove(_:))*