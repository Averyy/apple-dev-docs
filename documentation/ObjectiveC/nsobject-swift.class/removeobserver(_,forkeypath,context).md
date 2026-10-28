# removeObserver(_:forKeyPath:context:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath context:(void *) context;
```

## Discussion

Examining the value in `context` you are able to determine precisely which [`addObserver(_:forKeyPath:options:context:)`](./addobserver%28_,forkeypath,options,context%29.md) invocation was used to create the observation relationship. When the same observer is registered for the same key-path multiple times, but with different context pointers, an application can determine specifically which object to stop observing. It is an error to call [`removeObserver(_:forKeyPath:context:)`](./removeobserver%28_,forkeypath,context%29.md) if the object has not been registered as an observer.

Be sure to invoke this method (or [`removeObserver(_:forKeyPath:)`](./removeobserver%28_,forkeypath%29.md)) before any object specified in [`addObserver(_:forKeyPath:options:context:)`](./addobserver%28_,forkeypath,options,context%29.md) is deallocated.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the observed object, for which `observer` is registered to receive KVO change notifications.
- `context`: Arbitrary data that more specifically identifies the observer to be removed.

## See Also

### Registering for Observation
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String)](./removeobserver%28_,forkeypath%29.md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:context:))*