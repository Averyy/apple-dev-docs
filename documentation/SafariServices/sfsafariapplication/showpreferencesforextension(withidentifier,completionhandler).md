# showPreferencesForExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

Launches Safari and opens the preferences panel for a Safari app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func showPreferencesForExtension(withIdentifier identifier: String, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func showPreferencesForExtension(withIdentifier identifier: String) async throws
```

```objc
+ (void) showPreferencesForExtensionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func showPreferencesForExtension(withIdentifier identifier: String) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `identifier`: The identifier for a Safari app extension in your app bundle.
- `completionHandler`: A completion handler called after the operation completes. The completion handler takes the following parameter:

  - **error**: If an error occurred, this parameter describes the error. If the operation succeeded, this parameter holds `nil`.

## See Also

### Working with Windows
- [class func getActiveWindow(completionHandler: (SFSafariWindow?) -> Void)](./getactivewindow%28completionhandler%29.md)
  Calls the completion handler with the active browser window.
- [class func openWindow(with: URL, completionHandler: ((SFSafariWindow?) -> Void)?)](./openwindow%28with,completionhandler%29.md)
  Opens a new window with the desired webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/showpreferencesforextension(withidentifier:completionhandler:))*