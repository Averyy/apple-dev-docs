# listTemplate(_:didSelect:completionHandler:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The user has selected an item in the list template.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
func listTemplate(_ listTemplate: CPListTemplate, didSelect item: CPListItem, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func listTemplate(_ listTemplate: CPListTemplate, didSelect item: CPListItem) async
```

```objc
- (void) listTemplate:(CPListTemplate *) listTemplate didSelectListItem:(CPListItem *) item completionHandler:(void (^)()) completionHandler;
```

## Discussion

Your app has an opportunity to perform any necessary operations to prepare for completing this item selection. The list template will display a spinner after a short delay.

You must call the completion block after your app has finished loading and updated its UI.

## Parameters

- `listTemplate`: The list template containing this item
- `item`: The item selected by the user
- `completionHandler`: A completion block you must call after you have updated your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedelegate/listtemplate(_:didselect:completionhandler:))*