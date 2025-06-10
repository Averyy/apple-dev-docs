# Configuring the View Controller for Your Custom Interface

**Framework**: SiriKit

Configure your view controller to replace or augment the default interface in Siri or Maps.

#### Overview

When displaying responses to the user, SiriKit provides a default interface for displaying the content of your response. Replace some or all of this default interface with custom views, which you might do to fully customize the user’s Siri-based interactions with your app. Another option is to augment the default interface with a single view, hiding portions of the default UI that your content might duplicate.

##### Requirements and Limitations

For all customizations, you provide a view controller whose views contain the information that you want to display. When replacing the default interface, SiriKit may create multiple instances of your view controller, and you must configure each one appropriately for the type of displayed content. When augmenting the default interface, SiriKit creates a single instance of your view controller.

While onscreen, your view controllers remain part of the foreground Siri or Maps interface until the user dismisses it. You can update your view controllers as needed using timers or other programmatic means. Your view controllers also receive the normal callbacks when they’re loaded, shown, and hidden. However, your view controllers don’t receive touch events or any other events while they’re onscreen, and you can’t add gesture recognizers to them. Therefore, never create an interface with controls or views that require user interactions.

##### Replace Some or All of the Default Interface

In iOS 11 and later, you can replace some or all of the default Siri or Maps interface. Before displaying an interface to the user, Siri builds a list of parameters—that is, instances of the [`INParameter`](https://developer.apple.com/documentation/intents/inparameter) class—representing the data it wants to display. Each parameter identifies a property of the intent or response object contained in the [`INInteraction`](https://developer.apple.com/documentation/intents/ininteraction) object that SiriKit provides.

After building the list of parameters, SiriKit creates one or more instances of your view controller and calls the [`configureView(for:of:interactiveBehavior:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:)) method of each one, passing it a specific set of parameters. When the [`configureView(for:of:interactiveBehavior:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:)) method is called, you must decide whether you want to provide a custom interface for the specified parameters. If you do, add subviews to the view controller’s root view and update those views with the parameter’s content.

Although SiriKit often passes only one parameter at a time to your [`configureView(for:of:interactiveBehavior:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:)) method, you can configure a view that displays content for any number of parameters. When calling the completion handler of your configuration method, provide SiriKit with the set of parameters that your interface displays. Before creating a new view controller with the next set of parameters, SiriKit checks to see if you already displayed those parameters. If you did, SiriKit does not ask you to display them again.

##### Augment the Default Interface

If you want to keep the default Siri or Maps interface and only augment it with your custom content, implement the [`configure(with:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configure(with:context:completion:)) method of your view controller. SiriKit instantiates your view controller and calls that method to configure your view controller’s view. The context parameter tells you where your view controller will be displayed, giving you an opportunity to display your content differently in Siri and Maps.

The figure below shows the high-level life cycle of your view controller when you configure it to augment the default interface. The system creates your view controller and calls its [`configure(with:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configure(with:context:completion:)) method, passing it the interaction object you need to configure your interface. Once configured, your view controller is presented onscreen with the rest of the Siri or Maps content.

![Loading an Intents UI extension and calling the methods of your view controller to configure your interface.](https://docs-assets.developer.apple.com/published/06d4f12fda57ac728f984ef77ffa2ace/media-2864766%402x.png)

> **Note**:  While a view controller is onscreen, Maps may call the [`configure(with:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configure(with:context:completion:)) method again to deliver updated information for you to display. For example, Maps calls this method when your Intents extension provides a status update for a booked ride. Use any follow-up calls to update your view controller’s interface.

When the user dismisses the Siri or Maps interface, the system releases its reference to your view controller and your Intents UI extension. Your view controllers should only display information. Do not try to save data or communicate with your app when your view controller moves offscreen.

> ❗ **Important**:  In iOS 11 and later, if your view controller implements both the [`configureView(for:of:interactiveBehavior:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:)) and [`configure(with:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configure(with:context:completion:)) methods, SiriKit calls only the [`configureView(for:of:interactiveBehavior:context:completion:)`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontrolling/configureview(for:of:interactivebehavior:context:completion:)) method.

##### Tips for Implementing Your View Controller

Here are some tips for implementing the view controller for your Intents UI extension:

-  Using your app’s color, imagery, and other design elements is a great way to add familiarity and convey the presence of your app within the Siri or Maps interfaces.
-  Wait until your view controller’s [`viewDidAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidAppear(_:)) method is called to start animations. Stop animations in your view controller’s [`viewWillDisappear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewWillDisappear(_:)) method.
-  Your view controller may not be onscreen for very long, so use local resources and the provided [`INInteraction`](https://developer.apple.com/documentation/intents/ininteraction) object for the bulk of your configuration. If you need to fetch more information from a server, always do so asynchronously and update your interface later.
-  The provided [`INInteraction`](https://developer.apple.com/documentation/intents/ininteraction) object contains the original intent and the response provided by your Intents extension, which runs in a separate process. Using only the provided interaction object ensures that your view controller’s interface accurately reflects the information provided by your Intents extension. To communicate more information to your Intents UI app extension, your Intents app extension can include a custom [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object with its response and put the additional information in that object’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary.
-  You may include branding and information that is relevant to the user, but advertising is prohibited.
-  When calling the handler block of your configuration method, specify [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) for the size when you do not want the view controller to be shown onscreen. You might hide the view controller when there is no additional information to display for the specified intent.
-  When the context parameter is set to [`INUIHostedViewContext.mapsCard`](https://developer.apple.com/documentation/intentsui/inuihostedviewcontext/mapscard), do not include an [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView) in your view controller’s interface. Maps already displays a map, so having two maps showing similar information would be confusing to users.
-  Your Intents UI app extension has only one initial view controller. Using child view controllers lets you encapsulate the behavior for for different intents or different views of an intent in one place. During configuration of your initial view controller, all you have to do is instantiate the appropriate child view controller and install its view in your interface.

##### Hiding Portions of the Default Interface

SiriKit lets you hide some types of content in the default interfaces using properties of the [`INUIHostedViewSiriProviding`](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding) protocol. If you are only augmenting the default interface with custom content, use these properties to avoid duplicating the content shown by Siri or Maps. For example, a ride booking app that adds a map to the default interface could implement the [`displaysMap`](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding/displaysmap) property and use it to hide the map in the default interface.

For more information about hiding portions of the default interface, see [`INUIHostedViewSiriProviding`](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding).

## See Also

- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/configuring-the-view-controller-for-your-custom-interface)*