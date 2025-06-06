# addObserver(_:forKeyPath:options:context:)

**Framework**: Objective-C Runtime  
**Kind**: method

Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.

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
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

#### Discussion

Neither the object receiving this message, nor `observer`, are retained. An object that calls this method must also eventually call either the [`removeObserver(_:forKeyPath:)`](nsobject-swift.class/removeobserver(_:forkeypath:).md) or [`removeObserver(_:forKeyPath:context:)`](nsobject-swift.class/removeobserver(_:forkeypath:context:).md) method to unregister the observer when participating in KVO.

## Parameters

- `observer`: The object to register for KVO notifications. The observer must implement the key-value observing method  .
- `keyPath`: The key path, relative to the object receiving this message, of the property to observe. This value must not be  .
- `options`: A combination of the   values that specifies what is included in observation notifications. For possible values, see  .
- `context`: Arbitrary data that is passed to   in  .

## See Also

- [func removeObserver(NSObject, forKeyPath: String)](nsobject-swift.class/removeobserver(_:forkeypath:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsobject-swift.class/removeobserver(_:forkeypath:context:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:))*