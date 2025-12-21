# addSharedObserver(_:forKey:options:context:)

**Framework**: Foundation  
**Kind**: method

Add a new observer to the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func addSharedObserver(_ observer: NSObject, forKey key: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

#### Discussion

This method works like `-[NSObject addObserver: forKey: options: context:]`, but observations on nested and computed properties are disallowed. Observers are not registered until `setSharedObservers` is called on the observable.

## Parameters

- `observer`: The observer object to register for KVO notifications.   The observer must implement the key-value observing method 
- `key`: Key of the property being observed. This cannot be a nested   key path or a computed property
- `options`: A combination of NSKeyValueObservingOptions values that   specify what is included in observation notifications. For possible values   see NSKeyValueObservingOptions.
- `context`: Arbitrary data which is passed to the observer object


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers/addsharedobserver(_:forkey:options:context:))*