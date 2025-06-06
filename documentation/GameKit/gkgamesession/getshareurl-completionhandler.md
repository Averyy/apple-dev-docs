# getShareURL(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Retrieves the URL used to share a game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func shareURL() async throws -> URL
```

#### Discussion

When a player clicks the Share or Invite button in your app, they have indicated they want to interact with another player. This method to retrieves a `URL` used to invite other players into the current game session.

The completion handler for this method returns an optional `URL` and `Error`. After ensuring you have a valid `URL`, you should immediately present the player with the option to share their game session by sending the `URL` to another player or friend. This is accomplished by configuring a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) and presenting it. You must implicitly unwrap the `URL` when creating the activity view controller. For example, the listing below presents the shared URL on an iPad.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/getshareurl(completionhandler:))*