# Session

**Framework**: Accessory Transport Extension  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A session type that the handler serves.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
associatedtype Session : AccessoryFeatureRuntimeSession
```

## Discussion

This associated type conforms to [`AccessoryFeatureRuntimeSession`](../accessoryfeatureruntimesession.md), and each feature pins it through that feature’s own `Handler` type alias, such as [`AccessoryWorker.FeatureSession.Handler`](../accessoryworker/featuresession/handler.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesessionhandler/session)*