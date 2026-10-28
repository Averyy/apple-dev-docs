# init(delegate:queue:)

**Framework**: External Accessory  
**Kind**: init  
**Role**: Initializer

Creates a browser object that scans for unconfigured accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)?, queue: dispatch_queue_t?)
```

```objc
- (instancetype) initWithDelegate:(id<EAWiFiUnconfiguredAccessoryBrowserDelegate>) delegate queue:(dispatch_queue_t) queue;
```

## Return Value

An initialized browser object.

## Discussion

This method is the designated initializer for `EAWiFiUnconfiguredAccessoryBrowser`. After initialization, an app can configure a browser object based on its interests.

## Parameters

- `delegate`: The object that you use to receive browser-related events.
- `queue`: The dispatch queue on which the delegate would like to receive events. If `nil`, the events will be on the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/init(delegate:queue:))*