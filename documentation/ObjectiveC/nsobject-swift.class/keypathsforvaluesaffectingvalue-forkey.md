# keyPathsForValuesAffectingValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a set of key paths for properties whose values affect the value of the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>
```

#### Discussion

When an observer for the key is registered with an instance of the receiving class, key-value observing itself automatically observes all of the key paths for the same instance, and sends change notifications for the key to the observer when the value for any of those key paths changes.

The default implementation of this method searches the receiving class for a method whose name matches the pattern `+keyPathsForValuesAffecting<Key>`, and returns the result of invoking that method if it is found. Any such method must return an NSSet. If no such method is found, an NSSet that is computed from information provided by previous invocations of the now-deprecated [`setKeys:triggerChangeNotificationsForDependentKey:`](nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:.md) method is returned, for backward binary compatibility.

You can override this method when the getter method of one of your properties computes a value to return using the values of other properties, including those that are located by key paths. Your override should typically call `super` and return a set that includes any members in the set that result from doing that (so as not to interfere with overrides of this method in superclasses).

> **Note**:  You must not override this method when you add a computed property to an existing class using a category, overriding methods in categories is unsupported. In that case, implement a matching `+keyPathsForValuesAffecting<Key>` to take advantage of this mechanism.

 You must not override this method when you add a computed property to an existing class using a category, overriding methods in categories is unsupported. In that case, implement a matching `+keyPathsForValuesAffecting<Key>` to take advantage of this mechanism.

## Parameters

- `key`: The key whose value is affected by the key paths.

## See Also

- [class func automaticallyNotifiesObservers(forKey: String) -> Bool](nsobject-swift.class/automaticallynotifiesobservers(forkey:).md)
  Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [protocol NSKeyValueObservingCustomization : NSObjectProtocol](../Foundation/NSKeyValueObservingCustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [var observationInfo: UnsafeMutableRawPointer?](nsobject-swift.class/observationinfo.md)
  Returns a pointer that identifies information about all of the observers that are registered with the observed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey:))*