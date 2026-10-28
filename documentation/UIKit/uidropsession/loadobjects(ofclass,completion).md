# loadObjects(ofClass:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates and loads a new instance of the specified class for each drag item in the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func loadObjects(ofClass aClass: any NSItemProviderReading.Type, completion: @escaping ([any NSItemProviderReading]) -> Void) -> Progress
```

```objc
- (NSProgress *) loadObjectsOfClass:(Class<NSItemProviderReading> *) aClass completion:(void (^)(NSArray<__kindof id<NSItemProviderReading>> *objects)) completion;
```

## Mentions

- [Making a view into a drop destination](../making-a-view-into-a-drop-destination.md)

## Return Value

An aggregate of the load progress for each object that is loaded.

## Discussion

You can use this method only in the drop interaction delegate’s implementation of the [`dropInteraction(_:performDrop:)`](../uidropinteractiondelegate/dropinteraction%28_,performdrop%29.md) method. This method is called after the user drops the items into the destination view.

The completion handler is called on the main queue. It provides an array of all objects created, in the same order that the drag items were added to the drag session.

## Parameters

- `aClass`: A class conforming to the [`NSItemProviderReading`](../../Foundation/nsitemproviderreading.md) protocol.
- `completion`: The block that is executed after all objects are loaded.

## Default Implementations

### UIDropSession Implementations
- [func loadObjects<T>(ofClass: T.Type, completion: ([T]) -> Void) -> Progress](./loadobjects%28ofclass,completion%29-3ab01.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession/loadobjects(ofclass:completion:))*