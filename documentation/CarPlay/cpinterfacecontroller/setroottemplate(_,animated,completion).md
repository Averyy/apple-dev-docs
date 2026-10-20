# setRootTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Sets the root template of the navigation hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

```objc
- (void) setRootTemplate:(CPTemplate *) rootTemplate animated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

If you set a root template when a navigation hierarchy already exists, CarPlay replaces the entire hierarchy.

CarPlay calls `completion` after it presents the template. The Boolean parameter is [`true`](../../Swift/true.md) when the presentation succeeds; otherwise, it’s [`false`](../../Swift/false.md) and CarPlay provides an error that describes the failure. CarPlay throws an exception if the presentation fails and you don’t provide a closure.

## Parameters

- `rootTemplate`: The template to use as the root of a new navigation hierarchy.
- `animated`: If [`true`](../../Swift/true.md), CarPlay animates the presentation of the template. CarPlay ignores this flag when there isn’t an existing navigation hierarchy to replace.
- `completion`: The closure CarPlay calls after it presents the template.

## See Also

### Configuring the Interface Controller
- [var delegate: (any CPInterfaceControllerDelegate)?](./delegate.md)
  An object that serves as the delegate to the interface controller.
- [protocol CPInterfaceControllerDelegate](../cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](./prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/setroottemplate(_:animated:completion:))*