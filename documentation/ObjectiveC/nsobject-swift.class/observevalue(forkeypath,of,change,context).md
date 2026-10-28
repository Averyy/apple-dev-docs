# observeValue(forKeyPath:of:change:context:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Informs the observing object when the value at the specified key path relative to the observed object has changed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)
```

```objc
- (void) observeValueForKeyPath:(NSString *) keyPath ofObject:(id) object change:(NSDictionary<NSString *,id> *) change context:(void *) context;
```

## Discussion

For an `object` to begin sending change notification messages for the value at `keyPath`, you send it an [`addObserver(_:forKeyPath:options:context:)`](./addobserver%28_,forkeypath,options,context%29.md) message, naming the observing object that should receive the messages. When you are done observing, and in particular before the observing object is deallocated, you send the observed object a [`removeObserver(_:forKeyPath:)`](./removeobserver%28_,forkeypath%29.md) or [`removeObserver(_:forKeyPath:context:)`](./removeobserver%28_,forkeypath,context%29.md) message to unregister the observer, and stop sending change notification messages.

## Parameters

- `keyPath`: The key path, relative to `object`, to the value that has changed.
- `object`: The source object of the key path `keyPath`.
- `change`: A dictionary that describes the changes that have been made to the value of the property at the key path `keyPath` relative to `object`. Entries are described in `Change Dictionary Keys`.
- `context`: The value that was provided when the observer was registered to receive key-value observation notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:))*