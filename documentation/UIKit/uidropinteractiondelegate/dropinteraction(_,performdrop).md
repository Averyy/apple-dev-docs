# dropInteraction(_:performDrop:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate it can request the item provider data from the session’s drag items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, performDrop session: any UIDropSession)
```

```objc
- (void) dropInteraction:(UIDropInteraction *) interaction performDrop:(id<UIDropSession>) session;
```

## Mentions

- [Making a view into a drop destination](../making-a-view-into-a-drop-destination.md)

## Discussion

You can request a drag item’s [`itemProvider`](../uidragitem/itemprovider.md) data within the scope of this method only and not at any other time.

To request the data, iterate over the session items calling [`loadObject(ofClass:completionHandler:)`](../../Foundation/nsitemprovider/loadobject%28ofclass,completionhandler%29-8ak5d.md) on each item’s item provider. For example, if you are expecting the drag items to be images, here’s how you can load each image:

```swift
func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
    for item in session.items {
        let itemProvider = item.itemProvider
        guard itemProvider.canLoadObject(ofClass: UIImage.self) 
        else {continue}

        itemProvider.loadObject(ofClass: UIImage.self, completionHandler: { (object, error) in
            if let image = object as? UIImage {
                DispatchQueue.main.async {
                    self.imageView.image = image
                }
            }
        })
    }
}
```

If you need to be more specific about the type of data to load, use one of the following methods to specify the desired data type using its uniform type identifier (UTI):

- [`loadDataRepresentation(forTypeIdentifier:completionHandler:)`](../../Foundation/nsitemprovider/loaddatarepresentation%28fortypeidentifier,completionhandler%29.md)
- [`loadFileRepresentation(forTypeIdentifier:completionHandler:)`](../../Foundation/nsitemprovider/loadfilerepresentation%28fortypeidentifier,completionhandler%29.md)
- [`loadInPlaceFileRepresentation(forTypeIdentifier:completionHandler:)`](../../Foundation/nsitemprovider/loadinplacefilerepresentation%28fortypeidentifier,completionhandler%29.md)

If you want only JPEG images, use the UTI for the JPEG image type:

```swift
import MobileCoreServices // for kUTTypeJPEG
func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
    for item in session.items {
        let itemProvider = item.itemProvider
        itemProvider.loadDataRepresentation(forTypeIdentifier: kUTTypeJPEG as String, completionHandler: { (data, error) in
            guard
                let data = data,
                let image = UIImage(data: data)
                else {return}
            
            DispatchQueue.main.async {
                self.imageView.image = image
            }        
        })
    }
}
```

You can also use the session’s convenience method [`loadObjects(ofClass:completion:)`](../uidropsession/loadobjects%28ofclass,completion%29.md) to load the data for an item. Note that the completion handler for this method is called on the main thread, which is not true when loading the data from the item provider.

```swift
func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
    session.loadObjects(ofClass: UIImage.self) { objects in
        guard let images = objects as? [UIImage] else {return}
        for image in images {
            self.imageView.image = image
        }
    }
}
```

When you ask the session or item provider to load its data, it gives you a [`Progress`](../../Foundation/progress.md) object. You can also get the progress for the session at a later time from its [`progress`](../../Foundation/progressreporting/progress.md) property.

The [`Progress`](../../Foundation/progress.md) object tells you how much of the data transfer is complete and if the transfer has finished. What’s more, it can be used to cancel, pause, and resume the data-load process.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The session containing the drag items.

## See Also

### Handling the drop
- [func dropInteraction(UIDropInteraction, canHandle: any UIDropSession) -> Bool](./dropinteraction%28_,canhandle%29.md)
  Asks the delegate whether it can handle the session’s drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:performdrop:))*