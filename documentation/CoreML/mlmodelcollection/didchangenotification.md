# didChangeNotification

**Framework**: Core ML  
**Kind**: property

The notification the framework sends when it receives an update to a model collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

#### Discussion

Register your app to get notifications when a model collection update is available by calling [`addObserver(forName:object:queue:using:)`](https://developer.apple.com/documentation/Foundation/NotificationCenter/addObserver(forName:object:queue:using:)).

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

Typically, you register for model collection notifications when your app needs to use the newest models as soon as the collection is available. Your app can always get the newest model collection by calling [`beginAccessingModelCollectionWithIdentifier:completionHandler:`](mlmodelcollection/beginaccessingmodelcollectionwithidentifier:completionhandler:.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/didchangenotification)*