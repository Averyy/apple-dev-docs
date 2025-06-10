# addObserver(_:forKeyPath:options:context:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## Parameters

- `observer`: The object to register for KVO notifications. The observer must implement the key-value observing method  doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue .
- `keyPath`: The key path, relative to the set, of the property to observe. This value must not be  .
- `options`: A combination of the   values that specifies what is included in observation notifications. For possible values, see  .
- `context`: Arbitrary data that is passed to   in  doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue .

## See Also

- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsset/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsset/removeobserver(_:forkeypath:).md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/addobserver(_:forkeypath:options:context:))*