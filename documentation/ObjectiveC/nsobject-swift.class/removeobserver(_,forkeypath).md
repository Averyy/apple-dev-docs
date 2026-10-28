# removeObserver(_:forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.

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
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

```objc
- (void) removeObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath;
```

## Discussion

It is an error to call [`removeObserver(_:forKeyPath:)`](./removeobserver%28_,forkeypath%29.md) for an `object` that has not previously been registered as an observer.

Be sure to invoke this method (or [`removeObserver(_:forKeyPath:context:)`](./removeobserver%28_,forkeypath,context%29.md)) before any object specified in [`addObserver(_:forKeyPath:options:context:)`](./addobserver%28_,forkeypath,options,context%29.md) is deallocated.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the object receiving this message, for which `observer` is registered to receive KVO change notifications.

## See Also

### Registering for Observation
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:))*