# addPasses(_:withCompletionHandler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Presents a user interface for adding multiple passes at once.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func addPasses(_ passes: [PKPass]) async -> PKPassLibraryAddPassesStatus
```

#### Discussion

Use this method when someone initiates an action that generates a single pass, like purchasing a concert ticket, or multiple passes, like checking into a multiconnection flight. Your app adds the pass to the person’s Wallet automatically with [`PKPassLibrary.Capability.backgroundAddPasses`](pkpasslibrary/capability/backgroundaddpasses.md), or they receive a prompt to confirm the overall action or review the passes individually. If you want to the person to review individual passes visually before adding them, use an instance of [`PKAddPassesViewController`](pkaddpassesviewcontroller.md).

## Parameters

- `passes`: The passes to add.
- `completion`: The completion handler that PassKit calls after the user selects an action. This handler takes the following parameter: - **`status`**: A  [`PKPassLibraryAddPassesStatus`](pkpasslibraryaddpassesstatus.md) value that indicates whether PassKit adds the passes. If the user selects to review the passes, PassKit sets the status to [`PKPassLibraryAddPassesStatus.shouldReviewPasses`](pkpasslibraryaddpassesstatus/shouldreviewpasses.md). In this case, you must present an instance of [`PKAddPassesViewController`](pkaddpassesviewcontroller.md) to let the user review and add the passes.

## See Also

- [func requestAuthorization(for: PKPassLibrary.Capability, completion: (PKPassLibrary.AuthorizationStatus) -> Void)](pkpasslibrary/requestauthorization(for:completion:).md)
  Requests a person’s authorization to use a pass library capability.
- [PKPassLibrary.AuthorizationStatus](pkpasslibrary/authorizationstatus.md)
  Statuses that indicate whether a person authorized your app to add a pass to their Wallet.
- [PKPassLibrary.Capability](pkpasslibrary/capability.md)
  Features for which your app can request authorization from a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/addpasses(_:withcompletionhandler:))*