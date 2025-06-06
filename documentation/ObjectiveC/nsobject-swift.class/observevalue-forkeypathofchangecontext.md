# observeValue(forKeyPath:of:change:context:)

**Framework**: Objective-C Runtime  
**Kind**: method

Informs the observing object when the value at the specified key path relative to the observed object has changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)
```

#### Discussion

For an `object` to begin sending change notification messages for the value at `keyPath`, you send it an [`addObserver(_:forKeyPath:options:context:)`](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md) message, naming the observing object that should receive the messages. When you are done observing, and in particular before the observing object is deallocated, you send the observed object a [`removeObserver(_:forKeyPath:)`](nsobject-swift.class/removeobserver(_:forkeypath:).md) or [`removeObserver(_:forKeyPath:context:)`](nsobject-swift.class/removeobserver(_:forkeypath:context:).md) message to unregister the observer, and stop sending change notification messages.

## Parameters

- `keyPath`: The key path, relative to  , to the value that has changed.
- `object`: The source object of the key path  .
- `change`: A dictionary that describes the changes that have been made to the value of the property at the key path   relative to  . Entries are described in  .
- `context`: The value that was provided when the observer was registered to receive key-value observation notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:))*