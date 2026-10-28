# preparePreviewOfSearchableItem(identifier:queryString:completionHandler:)

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func preparePreviewOfSearchableItem(identifier: String, queryString: String?, completionHandler handler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
optional func preparePreviewOfSearchableItem(identifier: String, queryString: String?) async throws
```

```objc
- (void) preparePreviewOfSearchableItemWithIdentifier:(NSString *) identifier queryString:(NSString *) queryString completionHandler:(void (^)(NSError *)) handler;
```

## Discussion

Use this method to prepare the content of the view controller with the data that the searchable item represents.

This method will be called only once. It will be called in the main thread before presenting the view controller. Heavy work potentially blocking the main thread should be avoided in this method.

## Parameters

- `identifier`: The identifier of the CSSearchableItem the user interacted with in Spotlight.
- `queryString`: The query string the user entered in Spotlight before interacting with the CSSearchableItem.
- `handler`: The completion handler should be called whenever the view is ready to be displayed. A loading spinner will be shown until the handler is called. It can be called asynchronously after the method has returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewingcontroller/preparepreviewofsearchableitem(identifier:querystring:completionhandler:))*