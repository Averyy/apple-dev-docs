# default

**Framework**: Foundation  
**Kind**: property

Returns the shared iCloud key-value store object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class var `default`: NSUbiquitousKeyValueStore { get }
```

#### Return Value

The shared iCloud key-value store object.

#### Discussion

An app must always use the default iCloud key-value store object to get and set values. This store is tied to the unique identifier string your app provides in its entitlement requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/default)*