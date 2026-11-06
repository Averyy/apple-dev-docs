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
associatedtype Session : AccessoryFeatureSession
```

## Discussion

This associated type conforms to [`AccessoryFeatureSession`](../accessoryfeaturesession.md), and each feature pins it through that feature’s own `Handler` type alias, such as [`AccessoryWorker.Handler`](../accessoryworker/handler.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesessionhandler/session)*