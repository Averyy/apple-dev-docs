# Using the CarPlay Simulator

**Framework**: CarPlay

Configure Simulator to run and debug your CarPlay-enabled app.

#### Overview

Simulator provides the ability to run your CarPlay-enabled app in a second window. The window behaves as the vehicle’s primary CarPlay display, and you can interact with it like you would a real CarPlay system. Simulator provides additional options for navigation apps that you can enable to check your map content at various screen sizes and resolutions.

Don’t use Simulator as your sole method of testing. Apple recommends that you also test in a vehicle or aftermarket system. If possible, use a device that supports wireless CarPlay. This allows you to use Xcode to debug your app while it’s running in a physical CarPlay environment.

##### Open the Carplay Simulator

Simulator doesn’t open the CarPlay window by default, but does keep it open for the rest of the session after you activate it. Simulator can’t display your CarPlay-enabled app unless it has the necessary entitlements. See [`Requesting CarPlay Entitlements`](requesting-carplay-entitlements.md) for more information.

To open the CarPlay window:

1. In Xcode, build and run your project using the iOS simulator.
2. From the Simulator menu bar, choose I/O > External Displays > CarPlay.

The CarPlay window is 800 x 480 pixels and uses a display scale of @2x, which represents the common configuration of many CarPlay systems.

##### Enable Additional Options for Navigation Apps

If you’re developing a CarPlay-enabled navigation app, enable CarPlay’s additional options in Simulator, which allows you to change the window’s width, height, and scale. Use this flexibility to ensure your map content renders in all recommended configurations.

Before launching Simulator, open Terminal and enter the following command:

```bash
defaults write com.apple.iphonesimulator CarPlayExtraOptions -bool YES
```

Apple recommends that you test your CarPlay-enabled app using the following configurations, at a minimum:

| Configuration | Width x height (pixels) | Scale |
| --- | --- | --- |
| Minimum | 748 x 456 | @2x |
| Portrait | 768 x 1024 | @2x |
| Standard | 800 x 480 | @2x |
| High-resolution | 1920 x 720 | @3x |

##### Go Beyond Simulator

Simulator is useful during development, but it doesn’t provide certain CarPlay features that Apple recommends you include when testing your CarPlay-enabled app.

For example, you can’t use Simulator to test:

- . A user often interacts with CarPlay without first unlocking their iPhone. Your CarPlay-enabled app must perform its primary functions when the iPhone is in a locked state.
- . Users interact with certain CarPlay features using Siri exclusively. Ensure that your CarPlay-enabled app works as you expect throughout these interactions.
- . You CarPlay app must be a good audio citizen. Be mindful that audio may come from other sources when CarPlay is active. If your CarPlay-enabled app isn’t playing audio, deactivate its audio session. For example, an audio navigation prompt should cause the vehicle’s radio volume to lower and then rise again after the prompt finishes.

## See Also

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/using-the-carplay-simulator)*