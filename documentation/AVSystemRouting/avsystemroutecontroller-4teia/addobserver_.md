# addObserver:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Adds an observer to receive notifications about system routing events.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (BOOL) addObserver:(id<AVSystemRouteControllerObserver>) observer;
```

#### Return Value

`YES` if the observer was successfully added; `NO` if the observer was already registered, if registration failed, or if a previous registration for the same observer was cleaned up due to the observer being deallocated.

#### Discussion

Use this method to register an observer that receives callbacks when people interact with system routes in the route picker. The observer must conform to the [`AVSystemRouteControllerObserver`](../avsystemroutecontrollerobserver-7p7a5.md) protocol and implement the required protocol method to handle routing events such as route activation and deactivation.

Important: Your app must declare support for extensions with the `MDESupportsUniversalURLPlayback` key and/or for specific protocols in the `MDESupportedProtocols` key of  the app’s `Info.plist`.  This observer will only be called back when a user selects a route that has been provided by an extension that matches one of your app’s specified supported protocols.

## Parameters

- `observer`: An object that conforms to [`AVSystemRouteControllerObserver`](../avsystemroutecontrollerobserver-7p7a5.md) to receive routing event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-4teia/addobserver:)*