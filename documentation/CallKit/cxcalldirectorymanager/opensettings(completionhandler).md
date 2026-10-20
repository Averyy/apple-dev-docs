# openSettings(completionHandler:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Opens the iOS Settings app and shows the Call Blocking & Identification settings.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func openSettings(completionHandler completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func openSettings() async throws
```

```objc
- (void) openSettingsWithCompletionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func openSettings() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Before a Call Directory extension can operate on incoming calls, the user must explicitly enable the extension in the iOS Settings app.

Use this method to open the Settings app and show the Call Blocking & Identification settings directly.

## Parameters

- `completion`: A block executed when the manager finishes opening the Call Directory panel.

  - **error**: If an error occurred, an error object indicating how the operation failed; otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/opensettings(completionhandler:))*