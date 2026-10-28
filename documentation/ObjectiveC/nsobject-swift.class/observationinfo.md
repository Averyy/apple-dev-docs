# observationInfo

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

Returns a pointer that identifies information about all of the observers that are registered with the observed object.

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
var observationInfo: UnsafeMutableRawPointer? { get set }
```

```objc
@property (nullable) void * observationInfo;
```

## Return Value

A pointer that identifies information about all of the observers that are registered with the observed object, the options that were used at registration-time, and so on.

## Discussion

The default implementation of this method retrieves the information from a global dictionary of observed objects keyed by memory addresses.

For improved performance, both this property and [`observationInfo`](./observationinfo.md) can be overridden to store the opaque data pointer in an instance variable. Overrides of this property must not attempt to send messages to the stored data.

## See Also

### Observing Customization
- [class func automaticallyNotifiesObservers(forKey: String) -> Bool](./automaticallynotifiesobservers%28forkey%29.md)
  Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [class func keyPathsForValuesAffectingValue(forKey: String) -> Set<String>](./keypathsforvaluesaffectingvalue%28forkey%29.md)
  Returns a set of key paths for properties whose values affect the value of the specified key.
- [protocol NSKeyValueObservingCustomization](../../Foundation/nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [+ setKeys:triggerChangeNotificationsForDependentKey:](./setkeys_triggerchangenotificationsfordependentkey_.md)
  Configures the observed object to post change notifications for a given property if any of the properties specified in a given array changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observationinfo)*