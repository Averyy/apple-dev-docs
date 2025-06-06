# init(itemProvider:)

**Framework**: UIKit  
**Kind**: init

Initializes a new drag item with a specified item provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(itemProvider: NSItemProvider)
```

#### Return Value

A drag item that the system initializes with the specified item provider.

#### Discussion

Provide an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object to create a new drag item. The item provider communicates the data that the drag-and-drop activity shares between processes.

## Parameters

- `itemProvider`: An instance of   that conveys the data or file to share during the drag-and-drop activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/init(itemprovider:))*