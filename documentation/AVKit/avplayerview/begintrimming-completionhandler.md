# beginTrimming(completionHandler:)

**Framework**: AVKit  
**Kind**: method

Puts the player view into trimming mode.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func beginTrimming() async -> AVPlayerViewTrimResult
```

## Mentions

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func beginTrimming() async -> AVPlayerViewTrimResult
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func beginTrimming() async -> AVPlayerViewTrimResult
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

An example implementation of the handler block is as follows:

```swift
@IBAction func beginTrimming(_ sender: AnyObject) {
    playerView.beginTrimming { result in
        if result == .okButton {
            // user selected Trim button (AVPlayerViewTrimResult.okButton)...
        } else {
            // user selected Cancel button (AVPlayerViewTrimResult.cancelButton)...
        }
    }
}
```

This method blocks until the user selects either the Trim or the Cancel button.

## Parameters

- `handler`: The result passed to the closure indicates whether the user clicked the Trim or Cancel button.

## See Also

- [var canBeginTrimming: Bool](avplayerview/canbegintrimming.md)
  A Boolean value that indicates whether the player view can begin trimming.
- [enum AVPlayerViewTrimResult](avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/begintrimming(completionhandler:))*