# activityItemSource()

**Framework**: UIKit  
**Kind**: method

The activity item object that can be used by an activity view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func activityItemSource() -> any UIActivityItemSource
```

#### Discussion

Use [`activityItemSource()`](uicloudsharingcontroller/activityitemsource().md), an object that conforms to the [`UIActivityItemSource`](uiactivityitemsource.md) protocol, when you want to include the CloudKit Sharing action as one of the action items in an instance of [`UIActivityViewController`](uiactivityviewcontroller.md).

Including [`activityItemSource()`](uicloudsharingcontroller/activityitemsource().md) in an activity view controller can be useful when your app’s user interface doesn’t have space to display a button dedicated to CloudKit Sharing. For instance, say your app already has an action button that lets the user share data with social media sites or other apps through an activity view controller. If you include [`activityItemSource()`](uicloudsharingcontroller/activityitemsource().md) as one of the activity view controller’s action items, the controller includes the action as a user-selectable option, thus eliminating the need for a second button in your app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/activityitemsource())*