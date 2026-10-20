# automaticallyNotifiesObservers(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.

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
class func automaticallyNotifiesObservers(forKey key: String) -> Bool
```

```objc
+ (BOOL) automaticallyNotifiesObserversForKey:(NSString *) key;
```

#### Return Value

[`YES`](../yes.md) if the key-value observing machinery should automatically invoke [`willChangeValue(forKey:)`](./willchangevalue%28forkey%29.md)/[`didChangeValue(forKey:)`](./didchangevalue%28forkey%29.md) and [`willChange(_:valuesAt:forKey:)`](./willchange%28_,valuesat,forkey%29.md)/[`didChange(_:valuesAt:forKey:)`](./didchange%28_,valuesat,forkey%29.md) whenever instances of the class receive key-value coding messages for the `key`, or mutating key-value-coding-compliant methods for the `key` are invoked; otherwise [`NO`](../no.md).

#### Discussion

The default implementation returns [`YES`](../yes.md). Starting in OS X 10.5, the default implementation of this method searches the receiving class for a method whose name matches the pattern `+automaticallyNotifiesObserversOf<Key>`, and returns the result of invoking that method if it is found. Any found methods must return `BOOL`. If no such method is found [`YES`](../yes.md) is returned.

## See Also

### Observing Customization
- [class func keyPathsForValuesAffectingValue(forKey: String) -> Set<String>](./keypathsforvaluesaffectingvalue%28forkey%29.md)
  Returns a set of key paths for properties whose values affect the value of the specified key.
- [protocol NSKeyValueObservingCustomization](../../Foundation/nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [var observationInfo: UnsafeMutableRawPointer?](./observationinfo.md)
  Returns a pointer that identifies information about all of the observers that are registered with the observed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey:))*