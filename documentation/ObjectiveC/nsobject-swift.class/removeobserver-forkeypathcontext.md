# removeObserver(_:forKeyPath:context:)

**Framework**: Objective-C Runtime  
**Kind**: method

Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context: UnsafeMutableRawPointer?)
```

#### Discussion

Examining the value in `context` you are able to determine precisely which [`addObserver(_:forKeyPath:options:context:)`](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md) invocation was used to create the observation relationship. When the same observer is registered for the same key-path multiple times, but with different context pointers, an application can determine specifically which object to stop observing. It is an error to call [`removeObserver(_:forKeyPath:context:)`](nsobject-swift.class/removeobserver(_:forkeypath:context:).md) if the object has not been registered as an observer.

Be sure to invoke this method (or [`removeObserver(_:forKeyPath:)`](nsobject-swift.class/removeobserver(_:forkeypath:).md)) before any object specified in [`addObserver(_:forKeyPath:options:context:)`](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md) is deallocated.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the observed object, for which   is registered to receive KVO change notifications.
- `context`: Arbitrary data that more specifically identifies the observer to be removed.

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md)
  Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String)](nsobject-swift.class/removeobserver(_:forkeypath:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:context:))*