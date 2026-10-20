# presentedItemOperationQueue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The operation queue in which to execute presenter-related messages.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var presentedItemOperationQueue: OperationQueue { get }
```

```objc
@property (retain, readonly) NSOperationQueue * presentedItemOperationQueue;
```

#### Discussion

As other objects and processes interact with the presented item, the system queues relevant messages for this presenter object on the operation queue in this property. For example, when another process attempts to read a file presented by this object, the system places an invocation of this object’s [`relinquishPresentedItem(toReader:)`](./relinquishpresenteditem%28toreader%29.md) method on the queue for execution. The other process must wait to read the file until that method is dequeued and executed. Requests for an object’s presented URL are not processed on this queue.

## See Also

### Accessing File Presenter Attributes
- [var presentedItemURL: URL?](./presenteditemurl.md)
  The URL of the presented file or directory.
- [var primaryPresentedItemURL: URL?](./primarypresenteditemurl.md)
  The URL of a secondary item’s primary presented file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemoperationqueue)*