---
url: https://developer.apple.com/design/human-interface-guidelines/game-center
framework: HIG
---

# Game Center

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

> **Updated 2025-06-09:** Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images.

Game Center is Apple’s social gaming network, which lets players track their progress and connect with friends across Apple platforms, and boosts the discovery of your game across players’ devices.

![A sketch of the Game Center icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/c985d4e00200a4f2dbb25e455793149c/technologies-Game-Center-intro~dark%402x.png)
Supporting Game Center in your game allows players to:
- Discover new games their friends are playing.
- Seamlessly invite friends to play.
- See the latest activity from their games across the system, in the Apple Games app, the App Store, notifications, and more.
By enabling the player activities listed above, supporting Game Center also helps surface your game to more players across Apple platforms.
You can add Game Center into your game using the GameKit framework, which provides a full-featured UI that makes it easy for players to access and view their Game Center data within your game. Alternatively, you can also use GameKit to present this data within your own custom UI. For developer guidance, see [GameKit](../GameKit.md).

## Accessing Game Center
To provide the best Game Center experience for your players, begin by determining whether the player is signed in to their Game Center account on the system when they launch your game. If they aren’t, initialize the player with Game Center at that time. This provides the most seamless user experience, and maximizes discovery opportunities for your game, such as in the Top Played chart and in social recommendations through players’ friends.

### Integrating the access point
The Game Center *access point* is an Apple-designed UI element that lets players view their Game Center profile and information without leaving your game. For developer guidance, see [Adding an access point to your game](../GameKit/adding-an-access-point-to-your-game.md).
![An iPhone screenshot of the game The Coast, on the title screen. The access point control, a circular button with a diagonal rocket symbol, sits in the upper corner on the leading edge.](https://docs-assets.developer.apple.com/published/9774fc7f07482493ee1559593dc08e53/games-access-point-collapsed%402x.png)
In iOS, iPadOS, and macOS the access point leads players to the Game Overlay, a system overlay that allows players to view their progress and start game activities.
![An illustration composed of an iPhone screenshot and an iPad screenshot, both of the game The Coast, with the Game Overlay appearing over the top of each. In the iPhone screenshot the overlay covers the entire screen, while in the iPad screenshot the overlay appears vertically on the trailing edge.](https://docs-assets.developer.apple.com/published/ecc46f7b41634affa66051458f5ff0ef/games-game-overlay~dark%402x.png)
In visionOS and tvOS, the access point leads players to the in-game dashboard, a full-screen view of a player’s Game Center activity that appears on top of your game.
**Display the access point in menu screens.** Consider adding the access point to the main menu or the settings area of your game. Avoid displaying the access point during active gameplay or in temporary splash screens, cinematic flows, or tutorials that might precede your game’s main menu screen.
**Avoid placing controls near the access point.** You can choose to present the access point at any of the four corners of the screen in a fixed position. Remember that the access point has both a collapsed and expanded version, so check whether the access point overlaps any important UI and controls and adjust your layout accordingly.

> **Note:** In visionOS, the locations of the access point vary based on game type, such as immersive or volume-based. For developer guidance, see [Adding an access point to your game](../GameKit/adding-an-access-point-to-your-game.md#Configure-the-access-point-on-visionOS).
**Consider pausing your game while the Game Overlay or dashboard is present.** Pausing your game can help players view their Game Center information without feeling like the game is continuing without them.

### Using custom UI
Your game can include custom links into the Game Overlay (in iOS, iPadOS, macOS) or the dashboard (in visionOS and tvOS). Your custom UI can deep-link into specific areas within both such as leaderboards or a player’s Game Center profile.
**Use the artwork Game Center provides in custom links.** When referencing Game Center features in custom UI, use the official artwork from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies). Preserve the appearance of this artwork and don’t adjust the dimensions or visual effects.
**Use the correct terminology in custom links.** The following table describes how to use Game Center terminology correctly so that you can avoid confusing players in custom UI.
| Term | Incorrect terms | Localization |
| --- | --- | --- |
| Game Center | GameKit, GameCenter, game center | Use the system-provided translation of *Game Center* |
| Game Center Profile | Profile, Account, Player Info | Use the system-provided translation of *Game Center* and localize *Profile* |
| Achievements | Awards, Trophies, Medals |  |
| Leaderboards | Rankings, Scores, Leaders |  |
| Challenges | Competitions |  |
| Add Friends | Add, Add Profiles, Include Friends |  |


## Achievements
Achievements give players an added incentive to stay engaged with your game. Game Center achievements appear in a collectible card format that highlights the player’s progress and showcases your artwork. For developer guidance, see [Rewarding players with achievements](../GameKit/rewarding-players-with-achievements.md).
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the Achievements overview screen.](https://docs-assets.developer.apple.com/published/026715959db42c83de8cc04dc399dd03/games-achievement-overlay%402x.png)
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the detail view of a single achievement.](https://docs-assets.developer.apple.com/published/fa2b92d24d82b3cae0748a731df621e8/games-achievement-overlay-detail%402x.png)

### Integrating achievements into your game
**Align with Game Center achievement states.** Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the Locked group. When you map your achievements to the four Game Center achievement states, you give players a consistent experience and you help them see at a glance the types of achievements your game offers.
**Determine a display order.** The order in which you upload achievements is the order in which they appear, so consider the order you want before uploading files. For example, you might want your achievements to appear in an order that corresponds to the most common path through your game.
**Be succinct when describing achievements.** The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text. Use title-style capitalization for the achievement title and sentence-style capitalization for the description.
![A diagram of an achievement card, with callouts indicating the achievement image, title, and description.](https://docs-assets.developer.apple.com/published/638f280a867c22c0b751e068870c92f5/games-achievement-anatomy~dark%402x.png)
**Give players a sense of progress.** When you use progressive achievements, the system displays player progress and provides encouraging messages like “Youʼre more than halfway to completing Great Lakes Freighter in The Coast. Keep going!” to help motivate players to complete them.

### Creating achievement images
**Design rich, high-quality images that help players feel rewarded.** Achievements are a prominent feature in Game Center UI, so it’s essential to design high-quality assets that catch the eye and encourage players to return to your game. Avoid reusing the same asset to represent more than one achievement. If you don’t provide an asset for an achievement, the card shows a placeholder image instead.
**Create artwork in the appropriate size and format.** The system applies a circular mask to your achievement image, so be sure to keep content centered. Use the following specifications to create images.

## Leaderboards
Leaderboards are a great way to encourage friendly competition within your game. When you adopt Game Center, players can easily check their ranking against friends and global players as well as receive notifications when their friends challenge them or pass their score on a leaderboard. You can take advantage of the system-designed UI or present leaderboard information within custom UI. For developer guidance, see [Encourage progress and competition with leaderboards](../GameKit/encourage-progress-and-competition-with-leaderboards.md).
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the Leaderboards overview screen.](https://docs-assets.developer.apple.com/published/63770530177075f25554a9eefa82a959/games-leaderboards-overlay%402x.png)
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the detail view of a single leaderboard.](https://docs-assets.developer.apple.com/published/825cea7230ad7958b60f681aef7bb407/games-leaderboards-detail%402x.png)
**Choose a leaderboard type.** Game Center supports two types of leaderboards: *classic* and *recurring*.
- A *classic leaderboard* tracks a player’s best all-time score. Classic leaderboards are always active with no ending. The following are examples of goals you might include in a classic leaderboard:
  - Strive for the most perfect score in a rhythm game.
  - Collect the most coins in a single dungeon run.
  - Achieve the longest continuous time in an endless runner.
- A *recurring leaderboard* resets based on a time interval you define, such as every week or every day. Recurring leaderboards can increase engagement by giving players more chances to take the lead. The following are examples of features that work well with recurring leaderboards:
  - Daily rotating puzzles
  - Seasonal or holiday-themed events
  - Weekly leaderboards for different battle modes
**Take advantage of leaderboard sets for multiple leaderboards.** Leaderboard sets are an organization system that can make it easier for players to find the board they’re looking for. Consider grouping leaderboard sets by themes or gameplay experiences, such as:
- Difficulty modes (Easy, Standard, Hard)
- Activity types (Combat, Crafting, Farming)
- Genres and themes (Disco, Pop, Rock)
**Add leaderboard images.** Leaderboard artwork gives you another opportunity to reinforce your game’s visual aesthetic. Aim to create a unique image for each leaderboard in your game that reflects and showcases the gameplay involved in leaderboard ranking. Leaderboards appear across the system, promoting ways for players to engage and compete with friends, and having compelling images helps attract players and gives them a sense of the experience.
For games that run in iOS, iPadOS, and macOS, use a single image for your leaderboard image. For games that run in tvOS, provide a set of images that animate when the artwork is in focus. To learn more about focus effects, see [Focus and selection](focus-and-selection.md). For help creating focusable images, download the tvOS template from [Apple Design Resources](https://developer.apple.com/design/resources/#tvos-apps). Use the following specifications to create leaderboard artwork.

> **Note:** Be mindful of how cropping might affect your leaderboard artwork. In iOS, iPadOS, and macOS, the system crops artwork for leaderboards that are part of a leaderboard set. In tvOS, the focus effect on leaderboard artwork may crop your images at the edges of some layers. Make sure your primary content stays comfortably visible in both these scenarios.

## Challenges
Challenges turn single player activities into multiplayer experiences with friends. Challenges are built on top of leaderboards and allow players to connect with their friends and participate in competitions with time limits. For developer documentation, see [Creating engaging challenges from leaderboards](../GameKit/creating-engaging-challenges-from-leaderboards.md).
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the Challenges overview screen.](https://docs-assets.developer.apple.com/published/63176e29afb5351d511719cafdf1bb0d/games-challenges-overlay%402x.png)
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the detail view of a single challenge.](https://docs-assets.developer.apple.com/published/ddfb071869dd7577f3e43f955f1b6ce7/games-challenges-overlay-detail%402x.png)
**Create engaging challenges.** Challenges are great for short, skill-based gameplay activities that have a clear way of gauging players’ accomplishments. Create challenges that take 1-5 minutes to play, with gameplay that players can complete individually. Examples of compelling challenges are:
- Complete the fastest lap in a racing level.
- Defeat the most enemies in a single round.
- Solve a daily puzzle with the fewest mistakes.
**Avoid creating challenges that track overall progress or personal best scores.** These can give regular players an unfair advantage. Instead, track players’ most recent score after each attempt at your challenge. This helps keep your challenge motivating by placing all players on a level playing field.
**Make it easy to jump into your challenge.** Players can access challenges through invitation links, the Game Overlay, or in the Games app in iOS, iPadOS, and macOS. Always deep-link to the exact mode or level where your challenge begins, and help first-time players complete any initial onboarding before beginning the challenge. For example, if your game requires a tutorial level to understand basic controls, launch the player into the tutorial first and present UI that lets them know your game automatically jumps into the challenge afterward.
![A diagram of a challenge card, with callouts indicating the challenge title, artwork, and number of players, and the system-provided gradient at the bottom of the card.](https://docs-assets.developer.apple.com/published/032867a2020dc1d5e98e90aba24fbd71/games-challenge-anatomy~dark%402x.png)
**Create high-quality artwork that encourages players to engage with your challenges.** The system shows your challenge’s artwork in the Game Overlay, Games app, and in the preview of an invitation link. Avoid placing the primary content of your artwork in an area where the challenge’s title and description might cover it. If you need to use text in your challenge image, provide the appropriate localized versions through App Store Connect or Xcode. Use the following specifications to create challenge artwork.
![A diagram of the layout for a challenge image, with callouts indicating the image size and cropped area.](https://docs-assets.developer.apple.com/published/4f0ba93bbf736c70516d4569838d47ca/games-challenge-image-specs~dark%402x.png)
| Attribute | Value |
| --- | --- |
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |


## Multiplayer activities
Game Center supports both real-time and turn-based multiplayer activities that make it easy to connect players with friends or other players. Players can access multiplayer gameplay through party codes, the Game Overlay, the dashboard, or in the Games app. For developer documentation, see [Creating activities for your game](../GameKit/creating-activities-for-your-game.md).
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the Multiplayer levels overview screen.](https://docs-assets.developer.apple.com/published/f89b2ebd744907258cc4543688d5d011/games-multiplayer-overlay%402x.png)
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the detail view of a single multiplayer level.](https://docs-assets.developer.apple.com/published/b96755c00a2049def7aa3ce15c11c544/games-multiplayer-overlay-detail%402x.png)
**Use party codes to invite players to multiplayer activities.** Game Center party codes are a great way to coordinate real-time multiplayer sessions whether you use Game Center matchmaking and networking facilities or provide your own. Game Center generates alpha-numeric party codes that are typically eight characters long, such as “2MP4-9CMF.”  When integrating party codes into your multiplayer games, consider the following guidelines for the best player experience:
- Allow players to join gameplay late, leave early, and return later.
- Provide a way for players to view the current party code in your game.
- Allow players to enter a party code manually.
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the in-game UI for setting up or joining a multiplayer activity using a custom code.](https://docs-assets.developer.apple.com/published/21aa655690fc4f5ec113e47e587774ab/games-multiplayer-custom-code%402x.png)
**Support multiplayer activities through in-game UI.** The Game Overlay and Game Center dashboard help players find other people for a multiplayer match without leaving your game. Game Center’s default multiplayer interface lets a player invite nearby or recent players, Game Center friends, and contacts. You can also choose to present multiplayer functionality within your custom UI. For developer guidance, see [Finding multiple players for a game](../GameKit/finding-multiple-players-for-a-game.md).
![An iPhone screenshot of the game The Coast with the Game Overlay open, showing the in-game UI starting a multiplayer activity.](https://docs-assets.developer.apple.com/published/1b1d8dd189678fda25a18976d990b485/games-multiplayer-in-game-ui%402x.png)
**Provide engaging activity artwork.** Players see the preview image for a multiplayer activity throughout the system, such as in a party code, the Games app, or in-game UI. Use the following specifications to create your artwork.
![A diagram of a multiplayer activity card, with callouts indicating the activity title, artwork, and number of players, and the system-provided gradient at the bottom of the card.](https://docs-assets.developer.apple.com/published/8dc3e492a8a81de53a9de9a2bc7e6087/games-multiplayer-anatomy~dark%402x.png)
![A diagram of the layout for a multiplayer activity image, with callouts indicating the image size and cropped area.](https://docs-assets.developer.apple.com/published/4f0ba93bbf736c70516d4569838d47ca/games-multiplayer-image-specs~dark%402x.png)
| Attribute | Value |
| --- | --- |
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |


## Platform considerations
*No additional considerations for iOS, iPadOS, macOS, or visionOS.*

### tvOS
**Display an optional image at the top of the dashboard.** In tvOS, you can add an additional piece of artwork to the dashboard to highlight your game’s aesthetic. Use a simple, easily recognizable image that looks great at a distance. Consider using your game’s logo or word mark; however, don’t use your app icon for this image. Use the following specifications to create a dashboard image.
![A diagram of the layout for a tvOS dashboard image, with a callout indicating the image size.](https://docs-assets.developer.apple.com/published/f435320e26a225739319dd4e7a19e7cc/tvos-dashboard-image~dark%402x.png)
| Attribute | Value |
| --- | --- |
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |


### watchOS
**Be aware of Game Center support on watchOS.** While GameKit features and API are available for watchOS games, keep in mind that there’s no system-supported Game Center UI that you can invoke on watchOS. Instead, Game Center content for watchOS games appears on a connected iPhone.

## Resources

#### Related
[Designing for games](designing-for-games.md)
[Game controls](game-controls.md)
[Apple Design Resources](https://developer.apple.com/design/resources/#technologies)

#### Developer documentation
[GameKit](../GameKit.md)
[Creating activities for your game](../GameKit/creating-activities-for-your-game.md)
[Creating engaging challenges from leaderboards](../GameKit/creating-engaging-challenges-from-leaderboards.md)
[Create games for Apple platforms](https://developer.apple.com/games/)
[Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/)

#### Videos
- [Get started with Game Center](https://developer.apple.com/videos/play/wwdc2025/214) - Explore the features of Game Center and learn how to get started. We’ll show you best practices for implementing achievements, challenges, leaderboards, and activities to maximize your game’s discoverability, attract new players, and increase engagement.

To get the most out of this session, we also recommend watching “Engage players with the Apple Games app”.
- [Engage players with the Apple Games app](https://developer.apple.com/videos/play/wwdc2025/215) - Meet the Games app – a new destination for players to keep up with what’s happening in their games, discover new ones, and play with friends, all in one place. Learn how to set up your game for optimal visibility in the Games app, integrate Game Center to enable social play, and keep players coming back with In-App Events.

To get the most out of this session, we also recommend watching “Get started with Game Center”.

## Change log
| Date | Changes |
| --- | --- |
| June 9, 2025 | Added guidance for new challenges and multiplayer activities, and considerations for the Apple Games app and Game Overlay. Updated guidance and specifications for activity preview images. |
| February 2, 2024 | Added links to developer guidance on using the access point and dashboard in a visionOS game. |
| September 12, 2023 | Added artwork for the iOS achievement layout. |
| May 2, 2023 | Consolidated guidance into one page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/game-center](https://developer.apple.com/design/human-interface-guidelines/game-center)*
