# Rewarding players with achievements

**Framework**: GameKit

Use achievements to motivate players and engage them more in your game.

#### Overview

An  is a collectible item that a player receives as a reward for successfully reaching a particular goal in your game. Achievements provide players an additional way of engaging with your game, tracking gameplay progress, and sharing that progress with friends. You define the achievements available to players in your game, and Game Center saves the progress players make toward earning them. Players can view your game achievements and track their progress in the dashboard.

![An image of an iPhone screen in landscape layout, showing the Achievements section of the dashboard with three achievements — one completed, one in-progress, and one locked.](https://docs-assets.developer.apple.com/published/ae95236da22d2a840c22fac2b1e99bee/media-3729930%402x.png)

Your game can have a maximum of 100 achievements, 100 points per achievement, and 1000 points total for all achievements. To keep players engaged, you can progressively add achievements to each version of your game until you reach the limit.

For design guidance, see [`Human Interface Guidelines > Technologies > Game Center > Achievements`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-center#Achievements).

#### Configure and Test Achievements

Configure achievements in Xcode before accessing them in your code and testing locally with Game Progress Manager. When you’re ready to deploy your configuration, sync your updates with App Store Connect. For more information about configuring and testing Game Center features, see [`Initializing and configuring Game Center`](initializing-and-configuring-game-center.md).

When you configure an achievement in Xcode, you specify details like how many points the players earn for it, and whether they can earn the achievement more than once.

![A screenshot showing the Xcode project with a GameKit configuration file selected. An achievement is in a selected state and it shows a variety of properties to configure, like the reference name and point value.](https://docs-assets.developer.apple.com/published/1fe64e8b43979a11f6b5dfbb0d82ba89/xcode-config-achievements%402x.png)

You also localize the user-facing text and assets in each language and region you support, and specify whether to hide the achievement from players before they reach a goal in your game. If you don’t hide the achievement, Game Center shows it immediately in the locked state. Players can browse all the achievements in your game, including locked achievements, to learn more about them.

If you add an achievement to an unreleased version of your game or sign the game with a development certificate, Game Center annotates the achievement with a prerelease indicator. For example, if you run your game in Xcode, a prerelease indicator appears next to the achievement name and a message appears in the detail view. To change an achievement’s app version, see [`Add achievements to an app version`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/add-achievements-to-an-app-version).

Use the Game Progress Manager to test achievements on your local device before you push the configuration update to App Store Connect. After selecting an achievement, update the progress for it in the detail panel on the right. When the progress updates, the system sends an update to your app so you can verify that the achievement changes.

![A screenshot showing the Game Progress Manager with an achievement is in a selected state. The right panel shows the completion progress for the achievement that you can update to see it reflected in your local game.](https://docs-assets.developer.apple.com/published/af75ca8489bb71d74a68b8fe798d848f/xcode-progress-manager-achievements%402x.png)

For more information about the achievement properties you can configure, see [`Achievement properties`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/achievements).

#### Get the Object That Represents the Achievement

To start or continue reporting progress toward an achievement, you need a [`GKAchievement`](gkachievement.md) object that represents the achievement.

Load the in-progress achievements for the player using the [`loadAchievements(completionHandler:)`](gkachievement/loadachievements(completionhandler:).md) method. Use the identifier you enter in Xcode to find the corresponding `GKAchievement` object in the array that GameKit passes to the completion handler.

```swift
// Load the player's active achievements.
let achievements = try await GKAchievement.loadAchievements()
let achievementID = "101"

// Find an existing achievement.
var achievement = achievements.first(where: { $0.identifier == achievementID })

// Otherwise, create a new achievement.
if achievement == nil {
    achievement = GKAchievement(identifier: achievementID)
}
```

If the achievement isn’t in the array, your game hasn’t reported any progress toward this achievement for this player yet, and the dashboard shows it in the locked state. You must create a new [`GKAchievement`](gkachievement.md) object using the identifier from App Store Connect. For the local player, use the [`init(identifier:)`](gkachievement/init(identifier:).md) method to create the [`GKAchievement`](gkachievement.md) object. For another player, when ending a turn-based match, use the [`init(identifier:player:)`](gkachievement/init(identifier:player:).md) method.

#### Report the Players Progress

Initially, the percentage complete is `0` and the dashboard shows the achievement in the locked state. As the player progresses toward earning an achievement, you report the percentage the player completes for the achievement to Game Center.

Set the achievement’s [`percentComplete`](gkachievement/percentcomplete.md) property to a value between `0` and `100`. For example, increase the percentage complete by 10%.

```swift
achievement.percentComplete = achievement.percentComplete + 10.0
```

Then report the progress to Game Center by passing the achievement in an array to the [`report(_:withCompletionHandler:)`](gkachievement/report(_:withcompletionhandler:).md) method.

```swift
// Create an array containing the achievement.
let achievementsToReport: [GKAchievement] = [achievement]

// Report the progress to Game Center.
try await GKAchievement.report(achievementsToReport)
```

When reporting a percentage greater than `0` and less than `100`, the dashboard shows the achievement as in-progress. When you report that the player completes the achievement 100%, the dashboard shows the image for the achievement, and Game Center adds it to the player’s completed achievements.

GameKit also displays a banner notifying the player when they complete an achievement. If you want to display your own interface, set the [`showsCompletionBanner`](gkachievement/showscompletionbanner.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) before reporting the player’s progress so the default banner doesn’t appear.

You can also hide an achievement in Xcode when you configure it, and not report on the progress until the player completes it. For example, use a hidden achievement if an achievement description reveals aspects of your game’s plot, or if you want to surprise the player with awards.

If the player completes all achievements in your game or if you want to clear all progress the local player makes toward all their achievements, you can reset them using the [`resetAchievements(completionHandler:)`](gkachievement/resetachievements(completionhandler:).md) class method.

If you prefer to report progress through your own server, see [`Game Center player achievements`](https://developer.apple.com/documentation/AppStoreConnectAPI/game-center-player-achievements).

#### Show Achievements to Players

Players can view their achievements in the dashboard, which provides a familiar and consistent experience for users. You can add the access point to your game so players can open the dashboard and navigate to their achievements. The access point displays achievements in the highlights, and on the dashboard when the player opens it. You can also display the dashboard in the state that shows the achievements so players can drill down and navigate to their other Game Center data.

If you want to display the data directly in your interface, you can load details of all the achievements, including their identifiers and artwork, using the [`loadAchievementDescriptions(completionHandler:)`](gkachievementdescription/loadachievementdescriptions(completionhandler:).md) class method. GameKit returns the localized achievement titles and descriptions, which you provide when you configure the achievements in App Store Connect. To load the artwork for an achievement, use the [`loadImage(completionHandler:)`](gkachievementdescription/loadimage(completionhandler:).md) method.

## See Also

- [class GKAchievement](gkachievement.md)
  An achievement you can award a player as they make progress toward and reach a goal in your game.
- [class GKAchievementDescription](gkachievementdescription.md)
  An object containing the text and artwork used to present an achievement to a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/rewarding-players-with-achievements)*