# observationInfo

**Framework**: Objective-C Runtime  
**Kind**: property

Returns a pointer that identifies information about all of the observers that are registered with the observed object.

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
var observationInfo: UnsafeMutableRawPointer? { get set }
```

#### Return Value

A pointer that identifies information about all of the observers that are registered with the observed object, the options that were used at registration-time, and so on.

#### Discussion

The default implementation of this method retrieves the information from a global dictionary of observed objects keyed by memory addresses.

For improved performance, both this property and [`observationInfo`](nsobject-swift.class/observationinfo.md) can be overridden to store the opaque data pointer in an instance variable. Overrides of this property must not attempt to send messages to the stored data.

## See Also

- [class func automaticallyNotifiesObservers(forKey: String) -> Bool](nsobject-swift.class/automaticallynotifiesobservers(forkey:).md)
  Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [class func keyPathsForValuesAffectingValue(forKey: String) -> Set<String>](nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey:).md)
  Returns a set of key paths for properties whose values affect the value of the specified key.
- [protocol NSKeyValueObservingCustomization : NSObjectProtocol](../Foundation/NSKeyValueObservingCustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observationinfo)*