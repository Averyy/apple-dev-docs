# init(itemProvider:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new drag item with a specified item provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(itemProvider: NSItemProvider)
```

```objc
- (instancetype) initWithItemProvider:(NSItemProvider *) itemProvider;
```

#### Return Value

A drag item that the system initializes with the specified item provider.

#### Discussion

Provide an [`NSItemProvider`](../../Foundation/nsitemprovider.md) object to create a new drag item. The item provider communicates the data that the drag-and-drop activity shares between processes.

## Parameters

- `itemProvider`: An instance of [`NSItemProvider`](../../Foundation/nsitemprovider.md) that conveys the data or file to share during the drag-and-drop activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/init(itemprovider:))*