# fetchThumbnails(for:requestedSize:perThumbnailCompletionHandler:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Asks the file provider for a thumbnail of the specified items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func fetchThumbnails(for itemIdentifiers: [NSFileProviderItemIdentifier], requestedSize size: CGSize, perThumbnailCompletionHandler: @escaping (NSFileProviderItemIdentifier, Data?, (any Error)?) -> Void, completionHandler: @escaping ((any Error)?) -> Void) -> Progress
```

#### Return Value

An object that reports the progress of this request. If the thumbnails are no longer needed, the system can cancel this request by calling the progress object’s [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel()) method.

#### Discussion

For local files, the system automatically provides thumbnails for supported content types, and calls a Quick Look Preview extension to get thumbnails for custom types.

However, the system can’t generate thumbnails for remote items. Instead, it calls this method to request thumbnails for items stored on a remote sever. The system caches these thumbnails, and only requests thumbnails for new items as needed. The system caches thumbnails based on the item’s [`itemVersion`](nsfileprovideritemprotocol/itemversion.md) property. To update an item’s thumbnail, update the item’s version identifier.

In your implementation, call the `perThumbnailCompletionHandler` block once for each item in the `itemIdentifiers` array. Call the `completionHandler` block only after calling `perThumbnailCompletionHandler` for each item.

```swift
func fetchThumbnails(for itemIdentifiers: [NSFileProviderItemIdentifier], requestedSize size: CGSize, perThumbnailCompletionHandler: @escaping (NSFileProviderItemIdentifier, Data?, Error?) -> Void, completionHandler: @escaping (Error?) -> Void) -> Progress {
    
    let urlSession = URLSession(configuration: URLSessionConfiguration.default)
    let progress = Progress(totalUnitCount: Int64(itemIdentifiers.count))
    let group = DispatchGroup()
    
    for identifier in itemIdentifiers {
        // For simplicity, this sample downloads each thumbnail separately;
        // however, if possible, you should batch download all the thumbnails at once.
        
        // Create a request for the thumbnail from your server.
        let request = myURLRequestForThumbnail(identifier: identifier, size: size)
        
        // Enter the dispatch group.
        group.enter()
        
        // Download the thumbnail to disk.
        let downloadTask = urlSession.downloadTask(with: request, completionHandler: { (tempURL, response, error) in
            
            guard progress.isCancelled != true else {
                group.leave()
                return
            }
            
            var myErrorOrNil = error
            var mappedDataOrNil: Data? = nil
            
            // If the download succeeds, map a data object to the file.
            if let fileURL = tempURL  {
                do {
                    mappedDataOrNil = try Data(contentsOf:fileURL, options: Data.ReadingOptions.alwaysMapped)
                }
                catch let mappingError {
                    myErrorOrNil = mappingError
                }
            }
            
            // Call the per thumbnail completion handler for each thumbnail requested.
            perThumbnailCompletionHandler(identifier, mappedDataOrNil, myErrorOrNil)
            
            // Leave the dispatch group.
            group.leave()

        })
        
        // Add the download task's progress as a child to the overall progress.
        progress.addChild(downloadTask.progress, withPendingUnitCount: 1)
        
        // Start the download task.
        downloadTask.resume()
    }
    
    group.notify(queue: DispatchQueue.main) {
        // Call this completion handler once all thumbnails are complete.
        completionHandler(nil)
    }
    
    return progress
}
```

For the best performance, use PNG images for text and vector graphics, JPEG for nontransparent photographs, and JPEG2000 for photographs with transparent backgrounds; however, you can use any image formats supported by [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) and [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage). You can also select a different image type for different thumbnails.

If a global error occurs, you don’t have to call `perThumbnailCompletionHandler` on each item. Instead, call the `completionHandler` block, and pass in the global error. The system applies this error to all outstanding items.

If a given item doesn’t have a thumbnail, call the `perThumbnailCompletionHandler` block and pass `nil` for both the `imageData` and `error` parameters.

## Parameters

- `itemIdentifiers`: The identifiers of the specified items.
- `size`: The size for the thumbnail image.
- `perThumbnailCompletionHandler`: A block that you call once for each item in the   array. Pass the following parameters:
- `completionHandler`: A block that you call after returning a thumbnail for each item. Pass the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderthumbnailing/fetchthumbnails(for:requestedsize:perthumbnailcompletionhandler:completionhandler:))*