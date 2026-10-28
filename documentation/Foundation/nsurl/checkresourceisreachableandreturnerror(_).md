# checkResourceIsReachableAndReturnError(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns whether the resource pointed to by a file URL can be reached.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool
```

```objc
- (BOOL) checkResourceIsReachableAndReturnError:(NSError **) error;
```

## Return Value

[`true`](../../Swift/true.md) if the resource is reachable; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method synchronously checks if the file at the provided URL is reachable. Checking reachability is appropriate when making decisions that do not require other immediate operations on the resource, such as periodic maintenance of user interface state that depends on the existence of a specific document. For example, you might remove an item from a download list if the user deletes the file.

If your app must perform operations on the file, such as opening it or copying resource properties, it is more efficient to attempt the operation and handle any failure that may occur.

If this method returns [`false`](../../Swift/false.md), the object pointer referenced by `error` is populated with additional information.

## Parameters

- `error`: The error that occurred when the resource could not be reached.

## See Also

### Querying an NSURL
- [func isFileReferenceURL() -> Bool](./isfilereferenceurl%28%29.md)
  Returns whether the URL is a file reference URL.
- [var isFileURL: Bool](./isfileurl.md)
  A boolean value that determines whether the receiver is a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/checkresourceisreachableandreturnerror(_:))*