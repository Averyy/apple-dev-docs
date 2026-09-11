# Directing app intents to your app’s scenes

**Framework**: App Intents

Direct app intents to a specific SwiftUI or UIKit scene and use the app intent to configure the content of the scene.

#### Overview

Some app intent protocols cause your app to come to the foreground so it can display action-specific details. For example, an app intent based on the [`OpenIntent`](openintent.md) protocol tells your app to display content for a specific data item or entity, and an app intent based on the [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) protocol tells your app to display the results of a search. Instead of making any interface-related changes from your app intent’s [`perform()`](appintent/perform().md) method, a better approach is to make those changes from your scene code. To do that, you need the system to route relevant app intents to your app’s scenes, and you need to update your scene code to receive those app intents and update your views.

The system routes app intents to scenes with the help of the app intent’s target content identifier. This identifier is a custom string that you provide, although the framework also provides a default value you can use. In each of your scenes, you specify which target content identifiers the scene handles, and the system uses the information to match each app intent to the correct scene. After finding a matching scene, the system delivers the app intent to your custom code for handling.

> **Note**: Dispatching app intents to your SwiftUI and UIKit scenes is one option for updating your interface. For information about additional options, see [`Update your app’s interface using your app intent`](configuring-the-runtime-behavior-of-your-app-intents#Update-your-apps-interface-using-your-app-intent.md).

##### Update Your App Intent to Support Scene Based Routing

The system routes an app intent to one of your scenes only when the app intent implements the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol. If you’re building scenes using SwiftUI, add the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) protocol to any app intents you want the system to direct to those scenes. If you’re building scenes using UIKit, add the [`UISceneAppIntent`](uisceneappintent.md) protocol to your app intents instead. Both protocols add a default implementation of the [`contentIdentifier`](targetcontentprovidingintent/contentidentifier.md) property to your app intent, which provides the target content identifier the system needs to match your app intent to a scene. You can also add a custom implementation of the property to your app intent types if you want to supply a custom target content identifier for your type.

The following example shows an elided declaration of an app intent for a SwiftUI app that adopts the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) protocol. The app intent uses the default implementation of the [`contentIdentifier`](targetcontentprovidingintent/contentidentifier.md) property, which contains the persistent identifier for the app intent type. App intents set this identifier to the app intent type name by default.

```swift
struct ShowBrowserAppIntent: AppIntent, TargetContentProvidingIntent {
    // ...
}
```

> **Note**: If you don’t include the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol in an app intent, the system doesn’t route the app intent to one of your scenes.

##### Match Your App Intent to a Scene or View at Runtime

When the system prepares to run an app intent, it checks to see if the app intent implements the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol. If it does, the system examines the app’s scenes to determine if one of them wants to handle the app intent. If it finds a scene, the system dispatches the app intent to the scene before calling the app intent’s [`perform()`](appintent/perform().md) method. Your scene code uses the app intent to configure its views to display the associated information. After that configuration, the system brings your app to the foreground to display the content.

> ❗ **Important**: Make sure your app’s scene manifest includes the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes) key with the value set to `YES`, even if your app has only one scene. The App Intents framework requires support for multiple scenes to dispatch app intents to your scene at launch time. For information about how to configure your app’s scene manifest, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports).

When looking for a scene to handle an app intent, the system takes different approaches for SwiftUI and UIKit scenes. In your scene code, use the following techniques to tell the system which app intents your scene handles:

- In SwiftUI scenes, specify which app intents your scene handles by adding the [`handlesExternalEvents(preferring:allowing:)`](https://developer.apple.com/documentation/swiftui/view/handlesexternalevents(preferring:allowing:)) modifier to one of the scene’s views. Configure the modifier with the target content identifiers your scene prefers to handle and can handle. If none of the scene’s views has this modifier, the system matches app intents using the [`handlesExternalEvents(matching:)`](https://developer.apple.com/documentation/swiftui/scene/handlesexternalevents(matching:)) modifier on the scene itself.
- In UIKit scenes, specify which app intents your scene prefers, or can handle, using the scene’s [`activationConditions`](https://developer.apple.com/documentation/uikit/uiscene/activationconditions) property, which you configure in the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willconnectto:options:)) method when preparing the scene.

The system compares the target content identifier of an incoming app intent to the values you provide in your SwiftUI modifiers or scene activation conditions. If you don’t provide a custom target content identifier for your app intent, you can use only the type of the app intent to choose which scene you want. However, if you provide a custom value, you can incorporate additional information to help with the routing process. For example, you might include the ID of a relevant entity in the app intent, so you can pick the scene already displaying the same entity. The following example shows an app intent that incorporates entity-specific information into its target content identifier.

```swift
struct ShowBrowserAppIntent: AppIntent, TargetContentProvidingIntent {
    @Parameter var item : ItemEntity
    
    var contentIdentifier: String { "ShowBrowser:\(item.id.uuidString)" }

    //...
}
```

To direct an app intent to a specific SwiftUI scene, add the [`handlesExternalEvents(preferring:allowing:)`](https://developer.apple.com/documentation/swiftui/view/handlesexternalevents(preferring:allowing:)) modifier to one of the scene’s views. The following example shows a view that displays an entity. Because the view already displays the entity, it prefers to handle incoming requests when the target content identifier contains the entity’s identifier.  However, it also handles app intents that contain other entities.

```swift
struct BrowserView: View {
    @State private var item: ItemEntity
    
    init(item: ItemEntity) {
        self.item = item
    }
    
    var body: some View {
        VStack {
            Text("The item's name is: \(item.title)")
        }
        .padding()
        .handlesExternalEvents(preferring: (["ShowBrowser:" + item.id.uuidString]), allowing: ["*"])
    }
}
```

To configure the activation conditions in a UIKit scene, create predicates to match the target content identifiers of any incoming app intents. For an example of how to configure these activation conditions, see [`Supporting multiple windows on iPad`](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad).

##### Configure the Contents of the Scene

After determining which scene handles an app intent, the system dispatches the app intent to the scene so it can configure its views. The dispatching process happens in the background, giving the scene a chance to configure its views before any changes become visible. The scene configuration also happens before the system calls the app intent’s [`perform()`](appintent/perform().md) method, giving you the opportunity to prepare your interface before the app intent does anything. For example, if the app intent plays a video, your scene needs to configure the views for the video before playback can start. To configure your scene:

- For SwiftUI scenes, add the [`onAppIntentExecution(_:perform:)`](https://developer.apple.com/documentation/swiftui/view/onappintentexecution(_:perform:)) modifier to a view in your scene.
- For UIKit scenes, implement the [`scene(_:willPerformAppIntent:)`](appintentscenedelegate/scene(_:willperformappintent:).md) method of the [`AppIntentSceneDelegate`](appintentscenedelegate.md) protocol in your scene’s delegate object.

In the implementation of your modifier or delegate method, extract data from the app intent and use it to configure the views in your scene. The following example retrieves the entity from the provided app intent and assigns it to the view. This behavior allows the view to update its content to display the content from the specified entity.

```swift
struct BrowserView: View {
    @State private var item: ItemEntity
    
    init(item: ItemEntity) {
        self.item = item
    }
    
    var body: some View {
        VStack {
            Text("The item's name is: \(item.title)")
        }
        .padding()
        .handlesExternalEvents(preferring: (["ShowBrowser:" + item.id.uuidString]), allowing: ["*"])
        .onAppIntentExecution(ShowSceneAppIntent.self) { intent in
            self.item = intent.item
        }
    }
}
```

The system provides an additional way to configure scenes in UIKit apps. If you don’t implement the [`scene(_:willPerformAppIntent:)`](appintentscenedelegate/scene(_:willperformappintent:).md) method in your UIKit scene delegate, the system calls the [`performNavigation(forScene:)`](uisceneappintent/performnavigation(forscene:).md) method of the app intent instead. If you have several app intents that change the scene in different ways, you might prefer this approach over a single delegate method that switches behavior based on the app intent type. The [`performNavigation(forScene:)`](uisceneappintent/performnavigation(forscene:).md) method provides you with the scene to update, but you can also retrieve the scene from the [`uiScene`](uisceneappintent/uiscene.md) property the [`UISceneAppIntent`](uisceneappintent.md) protocol adds to your type.

## See Also

- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
  An interface that provides a custom identifier for an app intent.
- [protocol UISceneAppIntent](uisceneappintent.md)
  An interface you use to direct an app intent to a specific scene in your UIKit app.
- [protocol AppIntentSceneDelegate](appintentscenedelegate.md)
  The interface a UIKit scene delegate uses to receive an app intent and configure the scene’s views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/directing-app-intents-to-your-apps-scenes)*