# importDidFinish(completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Tells the File Provider extension that the system finished importing items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func importDidFinish(completionHandler: @escaping @Sendable () -> Void)
```

```swift
optional func importDidFinish() async
```

```objc
- (void) importDidFinishWithCompletionHandler:(void (^)()) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> optional func importDidFinish() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The system calls this method after importing on-disk items. You can trigger an import by calling either [`reimportItems(below:completionHandler:)`](../nsfileprovidermanager/reimportitems%28below,completionhandler%29.md) or [`import(_:fromDirectoryAt:completionHandler:)`](../nsfileprovidermanager/import%28_,fromdirectoryat,completionhandler%29.md). The system can also initiate its own imports as needed.

During the import, the system calls your File Provider extension’s [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](./createitem%28basedon,fields,contents,options,request,completionhandler%29.md) method and passes the [`mayAlreadyExist`](../nsfileprovidercreateitemoptions/mayalreadyexist.md) option. Check to see if the item already exists in your remote storage—uploading it if necessary.

After importing all the items, the system calls your [`importDidFinish(completionHandler:)`](./importdidfinish%28completionhandler%29.md) method. Handle any necessary cleanup operations, and then call the completion handler.

## Parameters

- `completionHandler`: A block that your implementation must call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/importdidfinish(completionhandler:))*