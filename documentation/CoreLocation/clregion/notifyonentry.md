# notifyOnEntry

**Framework**: Core Location  
**Kind**: property

A Boolean indicating that notifications are generated upon entry into the region.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
var notifyOnEntry: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/swift/true), a device crossing from outside the region to inside the region triggers the delivery of a notification. If the property is [`false`](https://developer.apple.com/documentation/swift/false), a notification is not generated. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

If the app is not running when a boundary crossing occurs, the system launches the app into the background to handle it. Upon launch, your app must configure new location manager and delegate objects to receive the notification. The notification is sent to your delegate’s [`locationManager(_:didEnterRegion:)`](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md) method.

## See Also

- [var notifyOnExit: Bool](clregion/notifyonexit.md)
  A Boolean indicating that notifications are generated upon exit from the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/notifyonentry)*