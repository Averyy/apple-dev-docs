# addObserver(_:forKeyPath:options:context:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Raises an exception.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

```objc
- (void) addObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath options:(NSKeyValueObservingOptions) options context:(void *) context;
```

#### Discussion

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## Parameters

- `observer`: The object to register for KVO notifications. The observer must implement the key-value observing method [`observeValue(forKeyPath:of:change:context:)`](../../ObjectiveC/nsobject-swift.class/observevalue%28forkeypath,of,change,context%29.md).
- `keyPath`: The key path, relative to the set, of the property to observe. This value must not be `nil`.
- `options`: A combination of the [`NSKeyValueObservingOptions`](../nskeyvalueobservingoptions.md) values that specifies what is included in observation notifications. For possible values, see [`NSKeyValueObservingOptions`](../nskeyvalueobservingoptions.md).
- `context`: Arbitrary data that is passed to `observer` in [`observeValue(forKeyPath:of:change:context:)`](../../ObjectiveC/nsobject-swift.class/observevalue%28forkeypath,of,change,context%29.md).

## See Also

### Key-Value Observing
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](./removeobserver%28_,forkeypath%29.md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/addobserver(_:forkeypath:options:context:))*