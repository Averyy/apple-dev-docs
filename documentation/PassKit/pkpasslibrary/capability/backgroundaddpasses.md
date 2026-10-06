# PKPassLibrary.Capability.backgroundAddPasses

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

A capability that lets your app add passes to Wallet automatically, without prompting the person to review or confirm each pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case backgroundAddPasses
```

#### Discussion

Request this capability when your app needs to add passes in the background, for example, after a purchase or a check-in, without interrupting the person with a confirmation prompt. If the person hasn’t granted this capability, call [`requestAuthorization(for:completion:)`](pkpasslibrary/requestauthorization(for:completion:).md) to ask for permission. If the person denies the request, present the passes for review instead by using an instance of [`PKAddPassesViewController`](pkaddpassesviewcontroller.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/capability/backgroundaddpasses)*