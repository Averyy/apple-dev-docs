# didChangeNotification

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

The notification the framework sends when it receives an update to a model collection.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const MLModelCollectionDidChangeNotification;
```

#### Discussion

Register your app to get notifications when a model collection update is available by calling [`addObserver(forName:object:queue:using:)`](../../Foundation/notificationcenter/addobserver%28forname,object,queue,using%29.md).

```swift
let center = NotificationCenter.default
var token: NSObjectProtocol?

token = center.addObserver(forName: MLModelCollection.didChangeNotification,
                           object: nil,
                           queue: nil) { [unowned self] note in
    guard let modelCollection = note.object as? MLModelCollection else {
        print("Model Collection notification's object is not a model collection")
        return
    }

    // Use updated model collection ...
    self.receivedUpdatedModelCollection(modelCollection)

    // Clean up notification registration.
    center.removeObserver(token!)
}
```

Typically, you register for model collection notifications when your app needs to use the newest models as soon as the collection is available. Your app can always get the newest model collection by calling [`beginAccessingModelCollectionWithIdentifier:completionHandler:`](./beginaccessingmodelcollectionwithidentifier_completionhandler_.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/didchangenotification)*