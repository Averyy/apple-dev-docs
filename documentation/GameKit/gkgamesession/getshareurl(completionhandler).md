# getShareURL(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the URL used to share a game session.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
func getShareURL(completionHandler: @escaping @Sendable (URL?, (any Error)?) -> Void)
```

```swift
func shareURL() async throws -> URL
```

```objc
- (void) getShareURLWithCompletionHandler:(void (^)(NSURL *url, NSError *error)) completionHandler;
```

#### Discussion

When a player clicks the Share or Invite button in your app, they have indicated they want to interact with another player. This method to retrieves a `URL` used to invite other players into the current game session.

The completion handler for this method returns an optional `URL` and `Error`. After ensuring you have a valid `URL`, you should immediately present the player with the option to share their game session by sending the `URL` to another player or friend. This is accomplished by configuring a [`UIActivityViewController`](../../UIKit/uiactivityviewcontroller.md) and presenting it. You must implicitly unwrap the `URL` when creating the activity view controller. For example, the listing below presents the shared URL on an iPad.

```objc
@IBAction func invitePlayerWithMessages(sender: UIButton) {
        myGameSession.getShareURL(completionHandler:  { (url, error) in
            if error == nil {
                let activityVC = UIActivityViewController.init(activityItems: [url!], applicationActivities: nil)
                activityVC.popoverPresentationController?.sourceView = sender
                self.present(activityVC, animated: true, completion: nil)
                
            } else {
                // .. Process the error
            }
        })
    }
```

After the URL has been shared, your app must handle any requests to join the game session.

## Parameters

- `completionHandler`: A block that is called after the shared URL has been retrieved.

  - **url**: An `NSURL` object that contains the URL sent to other players in order to invite them to a game session.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/getshareurl(completionhandler:))*