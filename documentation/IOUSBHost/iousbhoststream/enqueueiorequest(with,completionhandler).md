# enqueueIORequest(with:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enqueues an input/output request on the stream.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData?, completionHandler: (@Sendable (IOReturn, Int) -> Void)? = nil) throws
```

```swift
func enqueueIORequest(with data: NSMutableData?) async throws -> (IOReturn, Int)
```

```objc
- (BOOL) enqueueIORequestWithData:(NSMutableData *) data error:(NSError **) error completionHandler:(IOUSBHostCompletionHandler) completionHandler;
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func enqueueIORequest(with data: NSMutableData?) async throws -> (IOReturn, Int)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method sends an asynchronous request on the stream.

> **Note**:  Completion timeouts aren’t applicable to streams.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer.
- `completionHandler`: An [`IOUSBHostCompletionHandler`](../iousbhostcompletionhandler.md) that runs when the request completes. The `completionHandler` doesn’t run if the method returns an error.

## See Also

### Sending I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func abort(with: IOUSBHostAbortOption) throws](./abort%28with%29.md)
  Aborts pending input/output requests.
- [func abort() throws](./abort%28%29.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream/enqueueiorequest(with:completionhandler:))*