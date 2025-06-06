# removeObserver(_:forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method

Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.

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
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

#### Discussion

It is an error to call [`removeObserver(_:forKeyPath:)`](nsobject-swift.class/removeobserver(_:forkeypath:).md) for an `object` that has not previously been registered as an observer.

Be sure to invoke this method (or [`removeObserver(_:forKeyPath:context:)`](nsobject-swift.class/removeobserver(_:forkeypath:context:).md)) before any object specified in [`addObserver(_:forKeyPath:options:context:)`](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md) is deallocated.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the object receiving this message, for which   is registered to receive KVO change notifications.

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md)
  Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsobject-swift.class/removeobserver(_:forkeypath:context:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:))*