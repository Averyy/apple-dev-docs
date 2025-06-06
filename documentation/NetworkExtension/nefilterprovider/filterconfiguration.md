# filterConfiguration

**Framework**: Network Extension  
**Kind**: property

An [`NEFilterProviderConfiguration`](nefilterproviderconfiguration.md) object containing the current filter configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var filterConfiguration: NEFilterProviderConfiguration { get }
```

#### Discussion

The Filter Provider can observe this property to be notified when the configuration changes, using KVO. See [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider/filterconfiguration)*