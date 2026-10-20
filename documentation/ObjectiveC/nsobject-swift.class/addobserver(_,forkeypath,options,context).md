# addObserver(_:forKeyPath:options:context:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.

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
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

```objc
- (void) addObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath options:(NSKeyValueObservingOptions) options context:(void *) context;
```

#### Discussion

Neither the object receiving this message, nor `observer`, are retained. An object that calls this method must also eventually call either the [`removeObserver(_:forKeyPath:)`](./removeobserver%28_,forkeypath%29.md) or [`removeObserver(_:forKeyPath:context:)`](./removeobserver%28_,forkeypath,context%29.md) method to unregister the observer when participating in KVO.

## Parameters

- `observer`: The object to register for KVO notifications. The observer must implement the key-value observing method [`observeValue(forKeyPath:of:change:context:)`](./observevalue%28forkeypath,of,change,context%29.md).
- `keyPath`: The key path, relative to the object receiving this message, of the property to observe. This value must not be `nil`.
- `options`: A combination of the `NSKeyValueObservingOptions` values that specifies what is included in observation notifications. For possible values, see [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md).
- `context`: Arbitrary data that is passed to `observer` in [`observeValue(forKeyPath:of:change:context:)`](./observevalue%28forkeypath,of,change,context%29.md).

## See Also

### Registering for Observation
- [func removeObserver(NSObject, forKeyPath: String)](./removeobserver%28_,forkeypath%29.md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:))*