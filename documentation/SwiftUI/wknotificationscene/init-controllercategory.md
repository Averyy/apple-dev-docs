# init(controller:category:)

**Framework**: SwiftUI  
**Kind**: init

Creates a scene that appears in response to receiving a specific category of remote or local notifications.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(controller: Controller.Type = Controller.self, category: String)
```

#### Discussion

Use a watch notification instance to add support for one or more Apple Watch notification scenes that appear on receipt of the local or remote notification categories you specify. The example below, adds two notification scenes to the app declaration:

```swift
@main
struct PopQuizApp : App {
    var body: some Scene {
        MainScene {
            RootView()
        }

        WKNotificationScene(
            controller: QuizTimeController.self,
            category: "com.example.quiztime"
        )

        WKNotificationScene(
            controller: QuizResultsController.self,
            category: "com.example.results"
        )
    }
}
```

Each [`WKNotificationScene`](wknotificationscene.md) declaration references a [`WKUserNotificationHostingController`](wkusernotificationhostingcontroller.md) and a category string that you provide. The hosting controller displays your notification’s content view upon receipt of a local or a [`PushKit`](https://developer.apple.com/documentation/PushKit) notification. The category string you specify corresponds to the category name in the notification’s dictionary and describes a specific notification that contains the content displayed by the notification view.

## Parameters

- `controller`: The type of   to   display upon receipt of the specified notification category.
- `category`: The category of notifications to listen for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wknotificationscene/init(controller:category:))*