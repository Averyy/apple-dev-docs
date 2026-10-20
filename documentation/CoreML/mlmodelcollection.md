# MLModelCollection

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A set of Core ML models from a model deployment.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../Foundation/urlsession.md) instead.

## Declaration

```swift
class MLModelCollection
```

```objc
@interface MLModelCollection : NSObject
```

#### Overview

Use a model collection to access the models from a Core ML Model Deployment. For example, you can use a model collection to replace one or more of your app’s built-in models with a newer version.

To access the newest model collection from a deployment, call the [`beginAccessingModelCollectionWithIdentifier:completionHandler:`](./mlmodelcollection/beginaccessingmodelcollectionwithidentifier_completionhandler_.md) type method. Your app can also get a notification when Core ML receives an update to a model collection (see [`didChangeNotification`](./mlmodelcollection/didchangenotification.md)).

## Topics

### Accessing a model collection
- [class func endAccessing(identifier: String) async throws -> Bool](./mlmodelcollection/endaccessing%28identifier%29.md)
  Terminates access to a model collection.
### Identifying a model collection
- [var identifier: String](./mlmodelcollection/identifier.md)
  The name of the model collection, unique to the development team.
- [var deploymentID: String](./mlmodelcollection/deploymentid.md)
  The unique identifier of the model collection’s deployment.
### Retreiving models from a collection
- [var entries: [String : MLModelCollection.Entry]](./mlmodelcollection/entries.md)
  A dictionary of model entries keyed to the models’ identifiers.
- [MLModelCollection.Entry](./mlmodelcollection/entry.md)
  A model and its identifier within a model collection.
### Registering for model collection updates
- [class let didChangeNotification: NSNotification.Name](./mlmodelcollection/didchangenotification.md)
  The notification the framework sends when it receives an update to a model collection.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection)*