# getStateOfContentBlocker(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

Determines the state of your content blocker.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
class func getStateOfContentBlocker(withIdentifier identifier: String, completionHandler: @escaping @Sendable (SFContentBlockerState?, (any Error)?) -> Void)
```

```swift
class func stateOfContentBlocker(withIdentifier identifier: String) async throws -> SFContentBlockerState
```

```objc
+ (void) getStateOfContentBlockerWithIdentifier:(NSString *) identifier completionHandler:(void (^)(SFContentBlockerState *state, NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func stateOfContentBlocker(withIdentifier identifier: String) async throws -> SFContentBlockerState
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The `state` parameter of the completion handler’s `SFContentBlockerState` contains the [`isEnabled`](../sfcontentblockerstate/isenabled.md) property. If the content blocker is enabled, `state.isEnabled` is [`true`](../../Swift/true.md); otherwise it’s [`false`](../../Swift/false.md). See [`SFContentBlockerState`](../sfcontentblockerstate.md).

## Parameters

- `identifier`: The bundle identifier of your content blocker extension.
- `completionHandler`: The code block to invoke with the state of the content blocker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/getstateofcontentblocker(withidentifier:completionhandler:))*