# deauthorize(completion:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Invalidates a previously authorized right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func deauthorize(completion handler: @escaping @Sendable () -> Void)
```

```swift
func deauthorize() async
```

```objc
- (void) deauthorizeWithCompletion:(void (^)()) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func deauthorize() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/deauthorize(completion:))*