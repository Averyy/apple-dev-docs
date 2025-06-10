# Creating engaging challenges from leaderboards

**Framework**: GameKit

Encourage friendly competition by adding challenges to your game.

#### Overview

Challenges encourage your players to invite their friends into your game for friendly competitions in score-baseed rounds. Players will see your challenges promoted throughout the Games app and other places around the OS as suggestions for enjoying their games with friends. They can invite their Game Center friends and anyone from their contacts, see scores appear in real-time, get notified at key moments until a winner is crowned, and have a remach. Challenges are built on top of leaderboards, turning single-player game activities into a social experience players can share with their friends.

To adopt challenges, you just need an active Game Center leaderboard. When you associate a leaderboard with a challenge, the same scores submitted for that leaderboard will be submitted for players participating in the challenge automatically.

To learn more about the Games app, see [`Engage players with the Games app`](https://developer.apple.comhttps://developer.apple.com/wwdc25/215). To learn more about leaderboards that work well for challenges, see [`Choosing a leaderboard for your challenges`](choosing-a-leaderboard-for-your-challenges.md)

#### Configure Challenges

Before you can access challenges in your code, configure them in Xcode and sync the configuration updates with App Store Connect. Begin configuring a challenge by creating a GameKit configuration file.

1. In Xcode 16.3 and later, choose File > New > File from Template.
2. Choose  either iOS or  macOS as the platform.
3. Scroll down to Other, and select the GameKit File template.
4. Click Next.
5. In the sheet that appears, enter a name for the configuration and select the appropriate targets.
6. Click Create.

If you’ve already configured challenges in App Store Connect:

1. At the bottom of the left column, click the More (…) button.
2. Choose Pull from App Store Connect.
3. Select the bundle ID or Game Center group.
4. Click Pull

The details for the resource appear in the editor at right.

![A screenshot of the GameKit configuration in Xcode. The configuration includes a recurring leaderboard named Bubbles Popped and a challenge named Fastest Bubble Popped. The challenge is selected and shows the rules of the challenge, which include the challenge being repeatable. The challenge is associated with a recurring leaderboard so the duration rules are not configurable.](https://docs-assets.developer.apple.com/published/65e4be9c3b04bd6313a43d94aea2c573/challenges-fastest-popped-time%402x.png)

To create a new challenge, click the Add (+) button at the bottom of the left column, and choose Challenge. When you create a challenge, you specify details like the leaderboard to associate it with and the rules to apply, like repeatable and duration. You also configure localization details for the challenge, like the display name.

If you make changes to your game, like adding a new leaderboard or adding a deep link using activities, you can configure a minimum version for a challenge. When you do, the Games app prompts a person to upgrade to the appropriate version of your game to participate in the challenge. For more more information, see [`Manage Challenges`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/manage-challenges)

To learn more about the information you enter in App Store Connect, see [`Challenges`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/challenges).

#### Test Challenges By Using the Game Progress Manager

Game Progress Manager allows you to test your game features locally during development by modifying properties, reporting updates, and resetting resources. It also allows you to test leaderboard and deep links to your game. It also allows you to test leaderboard and deep links to your game.

Before testing your GameKit configuration, turn on Debug Mode in Xcode:

1. Choose Product > Scheme > Edit Scheme.
2. Select the Run configuration in the left column.
3. Select Options.
4. Scroll down to GameKit Configuration, and click the Enable Debug Mode checkbox.
5. Click Close.

To test your activity configuration, open the Game Progress Manager in Xcode:

1. Choose Debug > GameKit > Manage Game Progress.
2. In the sidebar, click the “Select a device” pop-up button, and select the physical device you use for testing.
3. Click the pop-up button beneath that and select the project you want to debug.

The test data stays local to your machine and doesn’t rely on App Store Connect to test.

> ❗ **Important**: Testing your app with the Game Progress Manager requires a physical device to test is available for iOS 18.4 and later, macOS 15.4 and later, tvOS 18.4 and later, and visionOS 2.4 and later.

After selecting the device and app, choose a leaderboard you want to test. In the inspector panel, you can trigger deep links to verify the behavior of your challenge.

> **Note**: When testing score submissions to a leaderboard, the system can notify you when they happen instead of needing to manually check. On iOS, open Settings > Developer and turn on Notify About Score Submissions.

#### Report Challenge Progress

Players can use the Games app to create challenges and invite their friends to play. After a player creates a challenge, you use the standard reporting methods for reporting updates to the leaderboard you associate with the challenge. When you use the leaderboard APIs, consider the following when providing a challenge experience:

- Submit scores at the end of the gameplay, like after a player finishes a race or scores their highest point value after a limited amount of time.
- Submit the most recent score the player earns at the end of an attempt.
- Rely on your leaderboard configuration to resolve a player’s personal best score instead of submitting their personal best.
- Use leaderboards to track attempts — not real-time scores — instead of submitting scores for each point a player earns.
- Game Center handles error recovery and offline score submission, so don’t submit scores during your game’s startup.

If you have a leaderboard that only tracks a player’s personal best or all time score, you can still use it for a challenge. Submit the most recent score with every attempt, but set the leaderboard’s Score Submission Type to Best Score. This will only display the player’s best score on the leaderboard, but also allow challenges to count the player’s most recent score submissions during the course of the challenge.

To help players navigate to the correct place when exploring your game, check your challenge definition to apply UI decorations.

```swift
// Check whether a definition has an active challenge.
if try await challengeDefinition.hasActiveChallenges {
    // Show a UI decoration.
}
```

To learn more about getting and submitting leaderboard scores, see [`Encourage progress and competition with leaderboards`](encourage-progress-and-competition-with-leaderboards.md).

#### Get the Object That Represents the Challenge

Use `GameKit` when you want to help facilitate challenge creation through your game. A [`GKChallengeDefinition`](gkchallengedefinition.md) class contains the static metadata you configure in Xcode or App Store Connect. Use `GKChallengeDefinition.all` to load all of the challenges that you define for a game:

```swift
// Load all challenges for a game.
let challengeDefinitions = try await GKChallengeDefinition.all
let challengeID = “com.example.mygame.challenge.sprint”
let leaderboardID = "com.example.mygame.leaderboard.highscore"

// Find a challenge definition by using an identifier.
let challenge = challengeDefinitions.first(where: { $0.identifier == challengeID })

// Find a leaderboard you associate with a challenge.
let leaderboard = challengeDefinitions.first(where: { $0.leaderboard?.baseLeaderboardID == leaderboardID })
```

#### Create a Challenge

If you don’t need to create a custom UI for challenge selection, use [`triggerForPlayTogether(handler:)`](gkaccesspoint/triggerforplaytogether(handler:).md) to present the default system UI that shows the available challenges for your game. After a player selects a challenge from the list, the view to create a challenge appears.

```swift
// Show the system UI to show a list of available challenges the player selects from.
await GKAccessPoint.shared.triggerForPlayTogether()
```

You can display the available challenges in your UI by fetching all of the challenge definitions. After a player selects the challenge they want to create, call [`trigger(challengeDefinitionID:handler:)`](gkaccesspoint/trigger(challengedefinitionid:handler:).md) with the challenge identifier. This UI gives the player a familiar experience to create a challenge from. When determining where to present the system UI for a challenge, consider placing entry points at contextually relevant locations in your game.

```swift
// Show the system UI to create a challenge based on the configuration.
await GKAccessPoint.shared.trigger(challengeDefinitionID: challenge.identifier)
```

#### Integrate Your Challenge with Activities

When you create an activity, you can associate it with a leaderboard that you use for challenges. When a player receives a challenge notification on their device, the system uses a deep link to help you navigate them into the experience.

When a player chooses to engage with your challenge, the system navigates them directly to it. For example, to configure a daily mini crossword challenge, perform the following steps:

1. Create a recurring leaderboard that restarts daily, specifying a start time and daily duration.
2. Create a game activity with a deep link to the crossword that you associate with the recurring leaderboard.
3. Configure the challenge with the recurring leaderboard and set it as not repeatable.

To learn more about adding activities to your game, and deep linking to them, see [`Creating activities for your game`](creating-activities-for-your-game.md)

## See Also

- [Choosing a leaderboard for your challenges](choosing-a-leaderboard-for-your-challenges.md)
  Understand what gameplay works well when configuring challenges in your game.
- [class GKChallengeDefinition](gkchallengedefinition.md)
  An object that represents the static metadata you define for the challenge.
- [GKShowChallengeBanners](../BundleResources/Information-Property-List/GKShowChallengeBanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards)*