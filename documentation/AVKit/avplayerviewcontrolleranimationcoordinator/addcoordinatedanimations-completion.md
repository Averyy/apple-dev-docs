# addCoordinatedAnimations(_:completion:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Adds animations to perform alongside the playback controls’ visibility animation.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `animations`: The animations to execute.
- `completion`: A closure to execute after the main animation completes. The system runs the specified animations in the same animation context as the main animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(_:completion:))*