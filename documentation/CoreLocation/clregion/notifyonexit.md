# notifyOnExit

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating that notifications are generated upon exit from the region.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
var notifyOnExit: Bool { get set }
```

```objc
@property (atomic, assign) BOOL notifyOnExit;
```

#### Discussion

When this property is [`true`](../../Swift/true.md), a device crossing from inside the region to outside the region triggers the delivery of a notification. If the property is [`false`](../../Swift/false.md), a notification is not generated. The default value of this property is [`true`](../../Swift/true.md).

If the app is not running when a boundary crossing occurs, the system launches the app into the background to handle it. Upon launch, your app must configure new location manager and delegate objects to receive the notification. The notification is sent to your delegate’s [`locationManager(_:didExitRegion:)`](../cllocationmanagerdelegate/locationmanager%28_,didexitregion%29.md) method.

## See Also

### Specifying the notification conditions
- [var notifyOnEntry: Bool](./notifyonentry.md)
  A Boolean indicating that notifications are generated upon entry into the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/notifyonexit)*