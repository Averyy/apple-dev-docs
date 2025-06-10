# fetchThumbnails(for:requestedSize:perThumbnailCompletionHandler:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Fetches the thumbnails for items that have been enumerated by the file provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func fetchThumbnails(for itemIdentifiers: [NSFileProviderItemIdentifier], requestedSize size: CGSize, perThumbnailCompletionHandler: @escaping (NSFileProviderItemIdentifier, Data?, (any Error)?) -> Void, completionHandler: @escaping ((any Error)?) -> Void) -> Progress
```

#### Return Value

An object that reports the progress of this request. If the thumbnails are no longer needed, the system can cancel this request by calling the progress object’s [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel()) method.

#### Discussion

For local files, the system automatically provides thumbnails for supported content types, and calls a Quick Look Preview extension to get thumbnails for custom types.

However, the system cannot generate thumbnails for remote items. Instead, it calls this method to request thumbnails for items stored on a remote sever. The system caches these thumbnails, and only requests thumbnails for new items as they are needed. Thumbnails are cached based on the item’s [`versionIdentifier`](nsfileprovideritemprotocol/versionidentifier.md) property. To update an item’s thumbnail, update the item’s version identifier.

In your implementation, call the `perThumbnailCompletionHandler` block once for each item in the `itemIdentifiers` array. Call the `completionHandler` block only after calling `perThumbnailCompletionHandler` for each item.

If a global error occurs, you do not have to call  `perThumbnailCompletionHandler` on each item. Instead, call the `completionHandler` block, and pass in the global error. The system applies this error to all outstanding items.

If a given item does not have a thumbnail, call the `perThumbnailCompletionHandler` block and pass `nil` for both the `imageData` and `error` parameters.

Listing 1 shows an example implementation.

Listing 1. Fetching thumbnails from a remote server.

```swift
override func fetchThumbnails(for itemIdentifiers: [NSFileProviderItemIdentifier], requestedSize size: CGSize, perThumbnailCompletionHandler: @escaping (NSFileProviderItemIdentifier, Data?, Error?) -> Void, completionHandler: @escaping (Error?) -> Void) -> Progress {
    
    let urlSession = URLSession(configuration: URLSessionConfiguration.default)
    let progress = Progress(totalUnitCount: Int64(itemIdentifiers.count))
    
    for identifier in itemIdentifiers {
        
        // Create a request for the thumbnail from your server.
        let request = myURLRequestForThumbnail(identifier: identifier, size: size)
        
        // Download the thumbnail to disk
        // For simplicity, this sample downloads each thumbnail separately;
        // however, if possible, you should batch download all the thumbnails at once.
        let downloadTask = urlSession.downloadTask(with: request, completionHandler: { (tempURL, response, error) in
            
            guard progress.isCancelled != true else {
                return
            }
            
            var myErrorOrNil = error
            var mappedDataOrNil: Data? = nil
            
            // If the download succeeds, map a data object to the file
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
            
            DispatchQueue.main.async {

                if progress.isFinished {
                    
                    // Call this completion handler once all thumbnails are complete
                    completionHandler(nil)
                }
            }
        })
        
        // Add the download task's progress as a child to the overall progress.
        progress.addChild(downloadTask.progress, withPendingUnitCount: 1)
        
        // Start the download task.
        downloadTask.resume()
    }
    
    return progress
}

```

## Parameters

- `itemIdentifiers`: The identifiers of the items that need thumbnails.
- `size`: The size of the thumbnails, in pixels.
- `perThumbnailCompletionHandler`: The completion handler for each thumbnail. Call this block once for each thumbnail returned. This completion handler takes the following parameters:
- `completionHandler`: The completion handler for the entire request. Call this block after all thumbnails have been returned. This completion handler takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/fetchthumbnails(for:requestedsize:perthumbnailcompletionhandler:completionhandler:))*