# GKChallengeDefinition

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

An object that represents the static metadata you define for the challenge.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class GKChallengeDefinition
```

```objc
@interface GKChallengeDefinition : NSObject
```

## Mentions

- [Creating engaging challenges from leaderboards](./creating-engaging-challenges-from-leaderboards.md)

## Topics

### Getting the display properties and image
- [var title: String](./gkchallengedefinition/title.md)
  A short title for the challenge definition.
- [var details: String?](./gkchallengedefinition/details.md)
  A more detailed description of the challenge definition.
- [func loadImage(completionHandler: (UIImage?, (any Error)?) -> Void)](./gkchallengedefinition/loadimage%28completionhandler%29.md)
  Loads the image set on the challenge definition, which may be `nil` if none was set.
### Getting the challenge rules
- [var durationOptions: [DateComponents]](./gkchallengedefinition/durationoptions.md)
  The duration options for the challenge, like `1 day` or `1 week`.
- [var isRepeatable: Bool](./gkchallengedefinition/isrepeatable.md)
  Indicates if a challenge can be attempted more than once.
### Getting the leaderboard
- [var leaderboard: GKLeaderboard?](./gkchallengedefinition/leaderboard.md)
  Scores submitted to this leaderboard will also be submitted as scores in this challenge.
### Getting the release state
- [var releaseState: GKReleaseState](./gkchallengedefinition/releasestate.md)
  The release state of the challenge definition in App Store Connect.
- [struct GKReleaseState](./gkreleasestate.md)
  Describes the release state of an App Store Connect resource, such as an Achievement or Leaderboard.
### Getting the identifier properties
- [var groupIdentifier: String?](./gkchallengedefinition/groupidentifier.md)
  The group identifier for the challenge definition, if one exists.
- [var identifier: String](./gkchallengedefinition/identifier.md)
  The developer defined identifier for a given challenge definition.
### Loading challenge definitions
- [class func loadChallengeDefinitions(completionHandler: ([GKChallengeDefinition]?, (any Error)?) -> Void)](./gkchallengedefinition/loadchallengedefinitions%28completionhandler%29.md)
  Loads all the challenge definitions for the current game, returns an empty array if none exist.
### Checking for active challenges
- [func hasActiveChallenges(completionHandler: (Bool, (any Error)?) -> Void)](./gkchallengedefinition/hasactivechallenges%28completionhandler%29.md)
  Indicates if this definition has active challenges associated with it.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Challenges
- [Creating engaging challenges from leaderboards](./creating-engaging-challenges-from-leaderboards.md)
  Encourage friendly competition by adding challenges to your game.
- [Choosing a leaderboard for your challenges](./choosing-a-leaderboard-for-your-challenges.md)
  Understand what gameplay works well when configuring challenges in your game.
- [GKShowChallengeBanners](../BundleResources/information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengedefinition)*