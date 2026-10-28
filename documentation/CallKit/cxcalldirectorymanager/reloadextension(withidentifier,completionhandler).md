# reloadExtension(withIdentifier:completionHandler:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously reloads the extension with the specified identifier.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func reloadExtension(withIdentifier identifier: String, completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func reloadExtension(withIdentifier identifier: String) async throws
```

```objc
- (void) reloadExtensionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func reloadExtension(withIdentifier identifier: String) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `identifier`: The identifier for the call extension.
- `completion`: A block to be executed when the manager is finished reloading the specified extension.

  - **error**: If an error occurred, an error object indicating how reloading failed, otherwise `nil`.

## See Also

### Working with a Call Directory App Extension
- [func getEnabledStatusForExtension(withIdentifier: String, completionHandler: (CXCallDirectoryManager.EnabledStatus, (any Error)?) -> Void)](./getenabledstatusforextension%28withidentifier,completionhandler%29.md)
  Asynchronously returns the enabled status of the extension with the specified identifier.
- [CXCallDirectoryManager.EnabledStatus](./enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](./getenabledstatusforextension%28withidentifier,completionhandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/reloadextension(withidentifier:completionhandler:))*